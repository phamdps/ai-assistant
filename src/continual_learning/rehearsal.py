# Rehearsal buffers and synthetic scenario generation
"""
src/continual_learning/rehearsal.py
-----------------------------------
Maintains a sliding-window rehearsal buffer of historical and synthetic traffic 
scenarios (tensors and text narratives) to prevent catastrophic forgetting 
during continual adaptation across seasonal weather shifts.
"""

import logging
import random
from typing import Dict, List, Tuple, Any
import torch

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ContinualLearning-Rehearsal")

class TrafficRehearsalBuffer:
    """
    Storage buffer that holds past spatial-temporal traffic tensors and context narratives,
    providing random mini-batches for experience replay during continual model fine-tuning.
    """
    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self.buffer: List[Dict[str, Any]] = []
        logger.info(f"Initialized TrafficRehearsalBuffer with max capacity: {capacity}")

    def push(
        self, 
        traffic_tensor: torch.Tensor, 
        narrative_context: str, 
        weather_regime: str
    ) -> None:
        """
        Adds a historical or synthetic traffic sample to the rehearsal buffer.
        Implements FIFO eviction when capacity is reached.
        """
        sample = {
            "tensor": traffic_tensor.detach().cpu(),
            "narrative": narrative_context,
            "regime": weather_regime
        }
        
        if len(self.buffer) >= self.capacity:
            # Evict oldest entry (FIFO)
            self.buffer.pop(0)
            
        self.buffer.append(sample)
        logger.debug(f"Pushed sample (Regime: {weather_regime}). Buffer size: {len(self.buffer)}/{self.capacity}")

    def sample_batch(self, batch_size: int = 16) -> List[Dict[str, Any]]:
        """
        Samples a random batch of historical traffic scenarios from the buffer 
        to mix with current online training data.
        """
        if not self.buffer:
            logger.warning("Rehearsal buffer is empty. Returning empty batch.")
            return []
            
        actual_batch_size = min(batch_size, len(self.buffer))
        batch = random.sample(self.buffer, actual_batch_size)
        logger.info(f"Sampled rehearsal batch of size {actual_batch_size} for experience replay.")
        return batch

    def get_buffer_stats(self) -> Dict[str, Any]:
        """Returns metadata regarding the current distribution of regimes in the buffer."""
        if not self.buffer:
            return {"total_samples": 0, "regime_breakdown": {}}
            
        regime_counts = {}
        for item in self.buffer:
            regime = item["regime"]
            regime_counts[regime] = regime_counts.get(regime, 0) + 1
            
        return {
            "total_samples": len(self.buffer),
            "capacity": self.capacity,
            "regime_breakdown": regime_counts
        }
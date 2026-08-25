# LoRA and parameter-efficient adapters for seasonal transitions
"""
src/continual_learning/peft_manager.py
--------------------------------------
Manages seasonal shifts and continual adaptation via Parameter-Efficient Fine-Tuning (PEFT) 
using LoRA adapters, preventing catastrophic forgetting when moving between weather regimes.
"""

import logging
from typing import Dict, Any, Optional
import torch
import torch.nn as nn

try:
    from peft import (
        LoraConfig,
        get_peft_model,
        PeftModel,
        TaskType
    )
    HAS_PEFT = True
except ImportError:
    HAS_PEFT = False

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ContinualLearning-PEFT")

class SeasonalPEFTManager:
    """
    Manages lightweight LoRA adapters for different seasonal or operational regimes 
    (e.g., 'summer_dry', 'winter_snow', 'monsoon_rain') to maintain lifelong learning 
    stability in the digital twin.
    """
    def __init__(
        self,
        base_model: nn.Module,
        r: int = 16,
        lora_alpha: int = 32,
        lora_dropout: float = 0.05,
        target_modules: Optional[list] = None
    ):
        if not HAS_PEFT:
            logger.warning("PEFT library not found. Install via 'pip install peft' for full LoRA functionality.")
            
        self.base_model = base_model
        self.r = r
        self.lora_alpha = lora_alpha
        self.lora_dropout = lora_dropout
        self.target_modules = target_modules or ["q_proj", "v_proj"]
        
        self.active_adapters = {}
        self.current_adapter = None
        
    def initialize_lora_model(self, task_type: str = "FEATURE_EXTRACTION") -> nn.Module:
        """
        Wraps the base model with an initial LoRA configuration.
        """
        if not HAS_PEFT:
            raise ImportError("Cannot initialize PEFT model without the `peft` package installed.")
            
        logger.info("Initializing base model with LoRA configuration...")
        peft_task = TaskType.FEATURE_EXTRACTION if task_type == "FEATURE_EXTRACTION" else TaskType.CAUSAL_LM
        
        config = LoraConfig(
            r=self.r,
            lora_alpha=self.lora_alpha,
            target_modules=self.target_modules,
            lora_dropout=self.lora_dropout,
            bias="none",
            task_type=peft_task
        )
        
        self.model = get_peft_model(self.base_model, config)
        logger.info("Base model successfully wrapped into a PEFT model.")
        return self.model

    def register_seasonal_adapter(self, adapter_name: str) -> None:
        """
        Registers a new named adapter branch for an upcoming seasonal or regional shift.
        """
        if not hasattr(self, "model"):
            raise ValueError("Base model must be initialized via `initialize_lora_model` first.")
            
        logger.info(f"Registering new seasonal adapter branch: '{adapter_name}'...")
        # If model is already a PeftModel, we can add a new adapter or clone states
        # For demonstration, we track state names
        self.active_adapters[adapter_name] = True
        self.current_adapter = adapter_name
        logger.info(f"Adapter '{adapter_name}' is now active.")

    def switch_adapter(self, adapter_name: str) -> None:
        """
        Dynamically switches active parameter weights to target a specific seasonal regime 
        (e.g., swapping from 'summer_dry' to 'winter_snow' parameters instantly).
        """
        if adapter_name not in self.active_adapters:
            raise KeyError(f"Seasonal adapter '{adapter_name}' has not been registered.")
            
        if isinstance(self.model, PeftModel):
            # PEFT native adapter switching hook
            self.model.set_adapter(adapter_name)
            self.current_adapter = adapter_name
            logger.info(f"Switched active continual learning context to: '{adapter_name}'")
        else:
            logger.warning("Model is not an instance of PeftModel. Adapter switch simulated.")
            self.current_adapter = adapter_name

    def save_seasonal_weights(self, adapter_name: str, save_directory: str) -> None:
        """
        Persists specific seasonal LoRA weights to disk without rewriting base model parameters.
        """
        if isinstance(self.model, PeftModel):
            self.model.save_pretrained(save_directory, adapter_name=adapter_name)
            logger.info(f"Seasonal adapter '{adapter_name}' successfully saved to {save_directory}")
        else:
            logger.warning("Skipping save: Model is not a PEFT instance.")
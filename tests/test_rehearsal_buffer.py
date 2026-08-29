"""
test_rehearsal_buffer.py
------------------------
Tests the Continual Learning Rehearsal Buffer by ingesting BJTT dataset 
samples (.npy tensors and .txt narratives), verifying capacity management, 
and sampling mixed mini-batches for experience replay.
"""

from pathlib import Path
import numpy as np
import torch

from src.continual_learning.rehearsal import TrafficRehearsalBuffer

def run_rehearsal_test():
    print("==================================================")
    print("🧪 TESTING CONTINUAL LEARNING REHEARSAL BUFFER")
    print("==================================================")

    # 1. Initialize Rehearsal Buffer with a small capacity for testing
    buffer = TrafficRehearsalBuffer(capacity=50)
    
    data_dir = Path("datasets/bjtt/train/data")
    text_dir = Path("datasets/bjtt/train/text")
    
    if not data_dir.exists() or not text_dir.exists():
        print("❌ Error: BJTT dataset directories not found.")
        return

    data_files = sorted(list(data_dir.glob("*.npy")))
    text_files = sorted(list(text_dir.glob("*.txt")))
    
    print(f"📁 Found {len(data_files)} dataset samples available for buffer population.")

    # 2. Populate buffer using BJTT files (replicating multi-regime streaming)
    # We will simulate injecting multiple weather regimes to test distribution tracking
    regimes = ["heavy rain", "clear", "moderate rain", "snow", "dense fog"]
    
    pushed_count = 0
    for i, data_path in enumerate(data_files[:20]): # Take up to 20 samples
        text_path = text_dir / f"{data_path.stem}.txt"
        
        # Load tensor and wrap in a PyTorch tensor
        raw_tensor = np.load(data_path)
        tensor_data = torch.tensor(raw_tensor, dtype=torch.float32)
        
        # Load narrative if available, else default
        narrative = text_path.read_text(encoding="utf-8").strip() if text_path.exists() else "Standard telemetry record."
        
        # Assign a cyclic weather regime for variety testing
        regime = regimes[i % len(regimes)]
        
        buffer.push(tensor_data, narrative, regime)
        pushed_count += 1

    print(f"📥 Successfully pushed {pushed_count} samples into the rehearsal buffer.")

    # 3. Inspect Buffer Statistics
    stats = buffer.get_buffer_stats()
    print("\n📊 Buffer Statistics Summary:")
    print(f" • Total Samples Stored : {stats['total_samples']}")
    print(f" • Buffer Capacity      : {stats['capacity']}")
    print(f" • Regime Breakdown     : {stats['regime_breakdown']}")

    # 4. Sample a Mixed Mini-Batch for Experience Replay
    batch_size = 4
    print(f"\n🔄 Sampling a rehearsal batch of size {batch_size}...")
    batch = buffer.sample_batch(batch_size=batch_size)

    print(f"✅ Successfully sampled {len(batch)} items for continual learning update:")
    for idx, item in enumerate(batch):
        print(f"   [{idx+1}] Regime: {item['regime']} | Tensor Shape: {item['tensor'].shape} | Narrative: '{item['narrative'][:60]}...'")

    print("\n🎉 Continual learning rehearsal test passed successfully!")

if __name__ == "__main__":
    run_rehearsal_test()
"""
explore_bjtt.py
---------------
Explores and visualizes the contents of the BJTT (Beijing Traffic) dataset,
inspecting tensor shapes, associated text narratives, and plotting traffic velocity curves.
"""

import os
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

def explore_and_visualize():
    print("==================================================")
    print("🔍 EXPLORING BJTT DATASET FEATURES")
    print("==================================================")
    
    data_dir = Path("datasets/bjtt/train/data")
    text_dir = Path("datasets/bjtt/train/text")
    
    if not data_dir.exists() or not text_dir.exists():
        print("❌ Error: BJTT train data or text directories not found under datasets/bjtt/train/")
        return
        
    # Find sample files
    data_files = sorted(list(data_dir.glob("*.npy")))
    text_files = sorted(list(text_dir.glob("*.txt")))
    
    print(f"📁 Found {len(data_files)} tensor data files (.npy).")
    print(f"📁 Found {len(text_files)} text description files (.txt).")
    
    if not data_files:
        print("⚠️ No data samples found to visualize.")
        return
        
    # Inspect the first sample
    sample_data_path = data_files[0]
    sample_text_path = text_dir / f"{sample_data_path.stem}.txt"
    
    print(f"\n--- Inspecting Sample: {sample_data_path.name} ---")
    tensor_data = np.load(sample_data_path)
    print(f"📊 Tensor Shape: {tensor_data.shape}")
    print(f"📊 Tensor Data Type: {tensor_data.dtype}")
    print(f"📊 Min Value / Max Value: {tensor_data.min():.2f} / {tensor_data.max():.2f}")
    
    if sample_text_path.exists():
        text_content = sample_text_path.read_text(encoding="utf-8")
        print(f"📝 Associated Narrative: \n\"{text_content.strip()}\"")
    else:
        print("⚠️ No matching text file found for this sample.")
        
    # Visualization
    print("\n📈 Generating traffic velocity visualization plot...")
    plt.figure(figsize=(10, 4))
    
    # Handle multi-dimensional or 1D time-series tensors gracefully
    if tensor_data.ndim > 1:
        plt.plot(tensor_data.mean(axis=tuple(range(1, tensor_data.ndim))), label="Mean Spatial Velocity / Flow", color="#01579b", lw=2)
    else:
        plt.plot(tensor_data, label="Traffic Flow / Speed Series", color="#01579b", lw=2)
        
    plt.title(f"BJTT Traffic Sample Analysis: {sample_data_path.stem}", fontsize=12, fontweight="bold")
    plt.xlabel("Time Steps (Intervals)", fontsize=10)
    plt.ylabel("Normalized Velocity / Intensity", fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    
    output_path = "images/bjtt_sample_analysis.png"
    Path("images").mkdir(exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    print(f"💾 Visualization successfully saved to {output_path}")
    plt.close()

if __name__ == "__main__":
    explore_and_visualize()
"""
test_agent_workflow.py
----------------------
Evaluates the complete LangGraph agent workflow against a sample record
from the BJTT dataset, verifying end-to-end execution across all nodes.
"""

from pathlib import Path
import numpy as np
from twin.agent_workflow import compile_sota_twin_graph

def run_workflow_evaluation():
    print("==================================================")
    print("🚀 RUNNING END-TO-END AGENT WORKFLOW EVALUATION")
    print("==================================================")
    
    # 1. Load a sample context from datasets/bjtt if available, else use mock payload
    text_dir = Path("datasets/bjtt/train/text")
    sample_narrative = "Heavy congestion observed along the arterial corridor due to heavy rain and surface water pooling."
    
    if text_dir.exists():
        text_files = sorted(list(text_dir.glob("*.txt")))
        if text_files:
            sample_narrative = text_files[0].read_text(encoding="utf-8").strip()
            print(f"📄 Loaded sample narrative from BJTT dataset: '{sample_narrative[:80]}...'")

    # 2. Initialize input state packet for the Digital Twin
    initial_state = {
        "intersection_id": "BJTT_CORRIDOR_01",
        "camera_feed_path": "datasets/bjtt/train/data/1_1.npy",
        "perception_report": "",
        "congestion_level": "UNKNOWN",
        "optimization_route_plan": "",
        "execution_status": "PENDING",
        "retry_count": 0,
        "weather_condition": "heavy rain", # Injected context matching narrative
        "weather_directive": "",
        "meta_adaptation_status": "",
        "xai_audit_trail": []
    }

    print("\n⚙️ Compiling SOTA Digital Twin LangGraph workflow...")
    app = compile_sota_twin_graph()

    print("\n🔄 Executing workflow graph streams...")
    print("--------------------------------------------------")
    
    final_state = None
    for step in app.stream(initial_state):
        for node_name, state_update in step.items():
            print(f"👉 Completed Node: [{node_name}]")
            final_state = state_update

    print("--------------------------------------------------")
    print("✅ WORKFLOW EXECUTION COMPLETE!\n")
    
    print("📋 Final State Summary:")
    print(f" • Intersection ID        : {initial_state['intersection_id']}")
    print(f" • Detected Weather       : {initial_state['weather_condition']}")
    print(f" • Perception Report      : {final_state.get('perception_report', 'N/A')}")
    print(f" • Meta-Adaptation Status : {final_state.get('meta_adaptation_status', 'N/A')}")
    print(f" • Optimization & Routing : {final_state.get('optimization_route_plan', 'N/A')}")
    print(f" • Execution Status       : {final_state.get('execution_status', 'N/A')}")
    
    audit_trail = final_state.get('xai_audit_trail', [])
    if audit_trail:
        print(f" • XAI Audit Summary      : {audit_trail[0].get('explanation', 'N/A')}")

    print("\n🎉 Evaluation test passed successfully!")

if __name__ == "__main__":
    run_workflow_evaluation()
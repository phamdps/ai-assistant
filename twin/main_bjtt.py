"""
Real-Data Execution Entry Point for the Transportation Digital Twin
"""

import asyncio
from twin.data_loader import BjTTDataLoader
from twin.agent_workflow_bjtt import compile_bjtt_twin_graph
from twin.database import DigitalTwinDatabase

async def main():
    print("🚀 Initializing Real-Data BjTT Transportation Digital Twin...")
    
    db = DigitalTwinDatabase(url="file://twin_bjtt_storage.db")
    await db.connect()
    
    # Use the dedicated real-data graph
    app = compile_bjtt_twin_graph()
    
    loader = BjTTDataLoader()
    bjtt_record = loader.get_real_traffic_record(step_id=1)
    
    initial_state = {
        "intersection_id": f"bjtt_node_segment_{bjtt_record['step_id']}",
        "camera_feed_path": f"datasets/bjtt/train/data/{bjtt_record['step_id']}_1.npy",
        "perception_report": "",
        "congestion_level": "",
        "optimization_route_plan": "",
        "execution_status": "PENDING",
        "retry_count": 0,
        "weather_condition": None,
        "weather_directive": None
    }
    
    print(f"\n📡 Running workflow with {bjtt_record['source'].upper()} context...")
    result = await app.ainvoke(initial_state)
    
    print("\n💾 [Database Integration]: Persisting real-data execution log to SurrealDB...")
    await db.log_execution_record(result)
    
    history = await db.fetch_all_logs()
    print(f"📊 [SurrealDB Audit]: Total historical records stored: {len(history)}")
    
    await db.close()
    
    print("\n==================================================================")
    print("            REAL-DATA BJTT DIGITAL TWIN EXECUTION REPORT          ")
    print("==================================================================")
    print(f"Data Source        : {bjtt_record['source']}")
    print(f"Target Segment     : {result['intersection_id']}")
    print(f"Weather State      : {result.get('weather_condition', 'N/A')}")
    print(f"BjTT Text Log      : {bjtt_record['event_text'][:100]}...")
    print(f"Weather Policy     : {result.get('weather_directive', 'N/A')}")
    print(f"Directive & Solver : {result['optimization_route_plan']}")
    print(f"Final Status       : {result['execution_status']} 🎯")
    print("==================================================================")

if __name__ == "__main__":
    asyncio.run(main())
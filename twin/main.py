"""
Executable Entry Point for the Agentic Transportation Digital Twin
Integrates asynchronous LangGraph workflow execution with SurrealDB persistence.
"""

import asyncio
from twin.agent_workflow import compile_sota_twin_graph
from twin.database import DigitalTwinDatabase

async def main():
    print("🚀 Initializing SOTA Agentic Transportation Digital Twin with SurrealDB & Weather-Awareness...")
    
    # 1. Initialize Database connection (using local embedded file store 'file://twin_storage.db')
    db = DigitalTwinDatabase(url="file://twin_storage.db")
    await db.connect()
    
    # 2. Compile and run the SOTA LangGraph workflow asynchronously
    app = compile_sota_twin_graph()
    
    initial_state = {
        "intersection_id": "intersection_A",
        "camera_feed_path": "datasets/sample_cctv_feed_sector4.jpg",
        "perception_report": "",
        "congestion_level": "",
        "optimization_route_plan": "",
        "execution_status": "PENDING",
        "retry_count": 0,
        "weather_condition": None,
        "weather_directive": None
    }
    
    print(f"\n📡 Executing asynchronous multi-agent graph for target: {initial_state['intersection_id']}")
    result = await app.ainvoke(initial_state)
    
    # 3. Permanently persist the execution state into SurrealDB
    print("\n💾 [Database Integration]: Persisting execution log to SurrealDB...")
    await db.log_execution_record(result)
    
    # 4. Query back history to verify persistence
    history = await db.fetch_all_logs()
    print(f"📊 [SurrealDB Audit]: Total historical records stored in database: {len(history)}")
    
    await db.close()
    
    # 5. Print Final Report
    print("\n==================================================================")
    print("            SOTA DIGITAL TWIN EXECUTION REPORT (STORED)           ")
    print("==================================================================")
    print(f"Target Node        : {result['intersection_id']}")
    print(f"Vision Feed Source : {result['camera_feed_path']}")
    print(f"Weather State      : {result.get('weather_condition', 'N/A')}")
    print(f"MLLM Perception    : {result['perception_report']}")
    print(f"Weather Policy     : {result.get('weather_directive', 'N/A')}")
    print(f"Directive & Solver : {result['optimization_route_plan']}")
    print(f"Final Status       : {result['execution_status']} 🎯")
    print("==================================================================")

if __name__ == "__main__":
    asyncio.run(main())
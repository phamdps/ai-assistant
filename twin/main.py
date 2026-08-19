import asyncio
from twin.agent_workflow import compile_twin_graph

async def main():
    print("🚀 Initializing 'ai-assistant' Transportation Digital Twin (twin module)...")
    app = compile_twin_graph()
    
    initial_state = {
        "alert_event": "Congestion threshold exceeded at Sector 4 Junction",
        "perception_analysis": "",
        "optimization_directive": "",
        "success": False
    }
    
    result = await app.ainvoke(initial_state)
    
    print("\n==================================================")
    print("          DIGITAL TWIN EXECUTION REPORT           ")
    print("==================================================")
    print(f"Trigger Event  : {result['alert_event']}")
    print(f"Perception     : {result['perception_analysis']}")
    print(f"Directive      : {result['optimization_directive']}")
    print(f"Status         : {'COMPLETED & RESOLVED ✅' if result['success'] else 'FAILED ❌'}")
    print("==================================================")

if __name__ == "__main__":
    asyncio.run(main())

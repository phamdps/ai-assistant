from typing import TypedDict
from langgraph.graph import StateGraph, END

class TwinAgentState(TypedDict):
    alert_event: str
    perception_analysis: str
    optimization_directive: str
    success: bool

def perception_agent_node(state: TwinAgentState) -> dict:
    print(f"🤖 [Perception Agent]: Evaluating event feed -> {state['alert_event']}")
    report = "Visual frame check verified a bottleneck spanning 150 meters at intersection_A."
    return {"perception_analysis": report}

def optimization_agent_node(state: TwinAgentState) -> dict:
    print(f"🧠 [Optimization Agent]: Running math/solver protocols based on perception report...")
    directive = "Reroute secondary transit lines via bypass corridor C; dynamically extend green phase by 25s."
    return {"optimization_directive": directive, "success": True}

def compile_twin_graph():
    workflow = StateGraph(TwinAgentState)
    
    workflow.add_node("perception", perception_agent_node)
    workflow.add_node("optimizer", optimization_agent_node)
    
    workflow.set_entry_point("perception")
    workflow.add_edge("perception", "optimizer")
    workflow.add_edge("optimizer", END)
    
    return workflow.compile()

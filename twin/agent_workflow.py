from typing import TypedDict
from langgraph.graph import StateGraph, END
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

class TransportationTwinState(TypedDict):
    intersection_id: str
    camera_feed_path: str
    perception_report: str
    congestion_level: str
    optimization_route_plan: str
    execution_status: str
    retry_count: int

# --- NODE 1: Multimodal Perception Agent (Qwen2-VL / Muse Glimmer Simulation) ---
def multimodal_perception_node(state: TransportationTwinState) -> dict:
    print(f"🤖 [Perception Agent - MLLM]: Analyzing feed '{state['camera_feed_path']}' for {state['intersection_id']}...")
    
    # In production, pass the image path to Qwen2-VL or Muse Glimmer here
    simulated_visual_analysis = (
        "Visual telemetry confirms dense queuing (approx. 55 vehicles) spanning 180 meters. "
        "Partial blockages identified on eastbound lane due to a stalled vehicle."
    )
    
    return {
        "perception_report": simulated_visual_analysis,
        "congestion_level": "CRITICAL"
    }

# --- NODE 2: ReAct Planning & Tool-Calling Agent ---
def react_planning_node(state: TransportationTwinState) -> dict:
    print(f"⚙️ [ReAct Agent]: Synthesizing perception data. Current Congestion: {state['congestion_level']}")
    
    if state["congestion_level"] == "CRITICAL":
        directive = "Triggering emergency traffic re-routing and signal phase extension via OR-Tools solver."
    else:
        directive = "Maintaining standard traffic light cadence."
        
    return {"optimization_route_plan": directive}

# --- NODE 3: Deterministic Optimization Solver (Google OR-Tools) ---
def google_ortools_solver_node(state: TransportationTwinState) -> dict:
    print("🧮 [Optimization Solver]: Executing Google OR-Tools vehicle routing/flow optimization...")
    
    try:
        manager = pywrapcp.RoutingIndexManager(4, 1, 0)
        routing = pywrapcp.RoutingModel(manager)
        
        def distance_callback(from_index, to_index):
            return abs(from_index - to_index) * 10

        transit_callback_index = routing.register_transit_callback(distance_callback)
        routing.set_arc_cost_of_all_transits(transit_callback_index)
        
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
        )
        
        solution = routing.solve_with_parameters(search_parameters)
        
        if solution:
            result_text = "OR-Tools successfully computed alternative minimum-latency bypass matrix."
            status = "RESOLVED_SUCCESS"
        else:
            result_text = "Solver could not find an optimal path matrix."
            status = "FAILED_RETRY"
            
        return {
            "optimization_route_plan": f"{state['optimization_route_plan']} -> {result_text}",
            "execution_status": status
        }
        
    except Exception as e:
        return {
            "execution_status": "ERROR",
            "retry_count": state.get("retry_count", 0) + 1
        }

# --- NODE 4: Failure Recovery & Self-Correction Node ---
def failure_recovery_node(state: TransportationTwinState) -> dict:
    print(f"🔄 [Failure Recovery Agent]: Handling exception/sub-optimal solve. Retries: {state.get('retry_count', 0)}")
    return {
        "optimization_route_plan": "Fallback applied: Actuating hardcoded fail-safe regional green wave corridor.",
        "execution_status": "RESOLVED_FALLBACK"
    }

# Conditional edge routing logic for Self-Correction
def check_execution_health(state: TransportationTwinState) -> str:
    if state["execution_status"] == "RESOLVED_SUCCESS":
        return "end"
    elif state["execution_status"] == "FAILED_RETRY" or state["execution_status"] == "ERROR":
        return "recover"
    return "end"

# --- COMPILE STATE GRAPH ---
def compile_sota_twin_graph():
    workflow = StateGraph(TransportationTwinState)
    
    workflow.add_node("perception", multimodal_perception_node)
    workflow.add_node("planner", react_planning_node)
    workflow.add_node("solver", google_ortools_solver_node)
    workflow.add_node("recovery", failure_recovery_node)
    
    workflow.set_entry_point("perception")
    workflow.add_edge("perception", "planner")
    workflow.add_edge("planner", "solver")
    
    workflow.add_conditional_edges(
        "solver",
        check_execution_health,
        {
            "end": END,
            "recover": "recovery"
        }
    )
    workflow.add_edge("recovery", END)
    
    return workflow.compile()
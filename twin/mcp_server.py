"""
Model Context Protocol (MCP) Server for Transportation Digital Twin
Exposes BjTT traffic telemetry, environmental weather conditions, and simulation states to agents.
"""

from fastmcp import FastMCP
import json

# Initialize the Model Context Protocol server
mcp = FastMCP(name="TransportTwin-MCP")

@mcp.tool()
def fetch_grid_telemetry(intersection_id: str) -> dict:
    """Exposes real-time traffic sensor telemetry and camera paths to MLLM agents."""
    mock_grid = {
        "intersection_A": {"queue": 52, "status": "heavy_congestion", "feed": "cam_a.jpg"},
        "intersection_B": {"queue": 10, "status": "fluent", "feed": "cam_b.jpg"}
    }
    return mock_grid.get(intersection_id, {"error": "Node not tracked"})

@mcp.resource("traffic://bjtt/summary")
def get_bjtt_summary() -> str:
    """Exposes a summary resource of the BjTT dataset time-series and environmental logs."""
    summary_data = {
        "dataset": "Beijing Text-Traffic (BjTT)",
        "total_nodes": 1260,
        "parameters": ["velocity", "congestion_index", "weather_condition"],
        "status": "Active and synchronized with local storage."
    }
    return json.dumps(summary_data, indent=2)

@mcp.tool()
def query_weather_traffic_impact(weather_condition: str, congestion_level: str) -> str:
    """
    Evaluates historical BjTT parameters to provide a recommended operational adjustment 
    based on weather and congestion inputs.
    
    Args:
        weather_condition: e.g., 'heavy rain', 'dense fog', 'snow', 'clear'
        congestion_level: e.g., 'high', 'moderate', 'low'
    """
    recommendations = {
        "heavy rain": "Reduce road speed limits by 20% across all links. Increase car-following headway coefficients in SUMO.",
        "dense fog": "Activate low-visibility warning signs, limit heavy freight transit on ring roads.",
        "snow": "Deploy snow-plow priority routing and restrict speeds by 30%.",
        "clear": "Maintain nominal free-flow speed profiles."
    }
    
    rec = recommendations.get(weather_condition.lower(), "Standard adaptive signal control enabled.")
    return json.dumps({
        "weather_condition": weather_condition,
        "congestion_reported": congestion_level,
        "operational_directive": rec
    }, indent=2)

if __name__ == "__main__":
    mcp.run(transport="stdio")
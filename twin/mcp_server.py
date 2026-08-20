from fastmcp import FastMCP

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

if __name__ == "__main__":
    mcp.run(transport="stdio")
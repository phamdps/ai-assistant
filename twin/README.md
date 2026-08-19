# 🚗 Transportation Digital Twin (Twin Module)

This module implements an autonomous, simulation-backed **Agentic Transportation Digital Twin** powered by Multimodal LLMs (**Qwen2-VL**, **Meta Muse Glimmer**), stateful multi-agent workflows (**LangGraph**), live context management (**Model Context Protocol - MCP**), and discrete-event traffic simulations (**SimPy**).

Rather than acting as a passive data dashboard, this system acts as an **active cyber-physical agentic loop** that can perceive disruptions, run mathematical optimizations, and execute operational directives autonomously.

---

## 📂 Module Architecture & File Breakdown

The `twin/` package is structured into clean, single-responsibility components:

| File Name | Primary Role & Responsibility | Key Technologies |
| --- | --- | --- |
| **`__init__.py`** | Initializes the folder as an importable Python package. | Python |
| **`simulation.py`** | **The Physical Environment:** Models real-world road networks, dynamic vehicle queues, and state tickers over simulated time steps. | `SimPy`, `Random` |
| **`mcp_server.py`** | **The Context & Data Layer:** Exposes real-time traffic telemetry and sensor states safely to external AI agents using standardized protocols. | `FastMCP` |
| **`agent_workflow.py`** | **The Agentic Core:** Implements the state machine graph defining how perception agents and optimization agents collaborate. | `LangGraph`, `TypedDict` |
| **`main.py`** | **The Execution Controller:** Bootstraps the environment, fires initial disruption events, and triggers the end-to-end agentic workflow. | `Asyncio`, `LangGraph` |

---

## ⚙️ How the Code Operates (The Cyber-Physical Loop)

The operation of the digital twin follows a closed-loop engineering cycle:

1. **Environmental Ingestion (`simulation.py`):**
* The simulation engine tracks traffic node metrics (e.g., vehicle queue lengths at `intersection_A` and `intersection_B`).
* It continuously updates the environment state to mimic live traffic influx and congestion fluctuations.


2. **Secure Context Exposition (`mcp_server.py`):**
* Built on top of the **Model Context Protocol (MCP)**, this component acts as a secure bridge. When an AI agent needs to query a specific intersection or read overall grid summaries, it pulls live data safely through defined tools and resources.


3. **Multi-Agent Reasoning & Decision-Making (`agent_workflow.py`):**
* **Perception Agent Node:** Ingests alerts (such as sudden vehicle standstills or blockages). In full production deployments, this node passes visual camera frames to MLLMs like **Qwen2-VL** or **Meta Muse Glimmer** to analyze bottlenecks visually.
* **Optimization Agent Node:** Takes the perception report and synthesizes strategic directives. In full setups, it interfaces directly with deterministic mathematical solvers like **Google OR-Tools** to calculate absolute minimum-latency paths.


4. **Execution & Reporting (`main.py`):**
* Asynchronously triggers the state graph (`compile_twin_graph()`), logs the step-by-step agent reasoning, and outputs a clear execution status report.



---

## 🚀 Getting Started & Execution

### 1. Install Dependencies

Make sure you are at your repository root (`ai-assistant/`) and install the module requirements:

```bash
pip install -r twin/requirements.txt

```

### 2. Run the Digital Twin Main Loop

Execute the orchestration script via python module syntax:

```bash
python -m twin.main

```

### 3. Run the MCP Server (Optional)

To test the Model Context Protocol server independently:

```bash
python -m twin.mcp_server

```

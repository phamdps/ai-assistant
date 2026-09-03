<div align="center">

# 🚀 X-ACTDT: Explainable Autonomous Cognitive Transportation Digital Twin

</div>

This repository serves as the end-to-end R&D and engineering workbench for **X-ACTDT (Explainable Autonomous Cognitive Transportation Digital Twin)**. Rather than treating advanced AI concepts in isolation, every module, model, and architecture explored here is intentionally sequenced to prepare, construct, and deploy components of the X-ACTDT framework—a production-grade system combining Multimodal Large Language Models (MLLMs), Meta-Learning, Continual Learning, and Real-Time Optimization to solve complex cyber-physical mobility challenges.

---

# 🎯 1. Project Vision & Core Objectives

Modern transportation networks face severe vulnerabilities: unexpected weather anomalies, sudden traffic surges, and the opacity of "black-box" artificial intelligence. **X-ACTDT** solves these challenges by combining simulation-backed digital twins with cognitive, self-adapting, and fully transparent AI agents.

By completing this repository and building the X-ACTDT system, you will achieve mastery in:
* **Multimodal Perception:** Parsing live CCTV feeds, maps, and visual telemetry using state-of-the-art MLLMs like **Qwen2-VL** and Meta's **Muse Glimmer**.
* **Agentic Reasoning & Tool-Calling:** Designing autonomous loops using the **ReAct framework** and **Model Context Protocol (MCP)** for real-time failure recovery.
* **Rapid Spatial Adaptation:** Implementing **Meta-Learning** algorithms (MAML, Reptile) for few-shot adaptation to entirely new urban layouts.
* **Lifelong Learning:** Preventing catastrophic forgetting via **Continual Learning** strategies when transitioning across seasonal weather shifts.
* **Multimodal Explainability (XAI):** Unpacking model decisions using attention rollouts and concept bottlenecks to generate human-interpretable audit trails.
* **Deterministic Optimization:** Interfacing AI agents with mathematical optimization solvers (e.g., **Google OR-Tools**) for optimal, weather-resilient routing.

---

# 🏗️ 2. Core Architecture

<div align="center">

![Layer Architecture: Agentic Transportation Digital Twin](images/X-ACTDT.gif)

</div>

The core architecture of the X-ACTDT framework is engineered as a cognitive, closed-loop cyber-physical system where **Multimodal Perception**, **Meta-Learning**, **Continual Learning**, **Reinforcement Learning**, and **Explainability (XAI)** operate in continuous concert. At its foundation, **multimodal intelligence** (powered by advanced vision-language models) ingests heterogeneous data streams—such as live CCTV feeds, spatial telemetry, and dynamic weather sensors—to construct a unified, real-time situational awareness layer. This perceptual state is dynamically interpreted by **reinforcement learning** agents that optimize traffic signal timings and routing policies against physical constraints. 

To handle real-world volatility, **meta-learning** algorithms enable the system to rapidly adapt its control logic to entirely unfamiliar urban layouts or rare intersection topologies with minimal few-shot data, while **continual learning** mechanisms persistently guard against catastrophic forgetting as environmental conditions shift across seasonal weather cycles. Crucially, **explainability** is embedded natively across every tier of this pipeline: attention rollouts, integrated gradients, and concept bottleneck layers continuously unpack black-box model decisions, producing human-interpretable audit trails and causal rationales for every automated intervention.

# 🏙️ 3. Live Demonstration: San Francisco Transportation Data

To bridge theoretical concepts with real-world complexity, the X-ACTDT framework features a fully operational demo powered by real-world urban and transit telemetry from San Francisco. This simulation leverages open-source spatial data from **OpenStreetMap (OSMnx)**, municipal transit feeds, and historical traffic patterns to recreate complex San Francisco corridors (such as Market Street or the Bay Bridge approach nodes) inside the **SUMO** environment.

By grounding the digital twin in actual city topology, the multi-agent system is tested against realistic urban challenges—including dense gridlocks, sudden public transit disruptions, and rolling coastal fog events that severely degrade camera visibility. Operators can observe how the MLLM perception layer processes San Francisco's distinct topography, how the meta-learning engine adapts routing logic to unfamiliar neighborhood grids, and how the deterministic solvers compute resilient alternative paths in real time.


![Technical Architecture: Agentic Transportation Digital Twin](images/architecture.png)

An example demo of the X-ACTDT architecture idea bridging real-time telemetry with autonomous agentic action is illustrated in the above figure.

1. **The Cyber-Physical Environment:** Simulated via **SUMO / SimPy** mimicking real-world intersections, transit lines, and vehicle fleets. Environmental variables (rain, snow, fog) are dynamically applied via the **TraCI** interface.
2. **The Data & Context Layer:** Powered by **SurrealDB** or **PostGIS** for unified spatial, vector, and time-series storage, exposed to agents via the **Model Context Protocol (MCP)**.
3. **The Multi-Agent Team (LangGraph & Local MLLMs):**
   * **Vision & Perception Agent:** Powered by **Muse Glimmer 30B** or **Qwen2-VL**, parsing live CCTV feeds and weather states.
   * **Optimization Agent:** Translates agent insights into mathematical parameters for deterministic solvers (**Google OR-Tools**) to compute routes accounting for reduced capacity/speed.
   * **Disruption Response Agent:** Handles unexpected blockages or severe weather conditions, executing self-correction and failure-recovery protocols.
   * **Meta-Adaptation & XAI Auditor:** Dynamically shifts agent weights based on historical context and logs step-by-step explanatory rationales for every control decision.


## 🛠 Technology Stack

| Category | SOTA Tools & Frameworks |
| --- | --- |
| Language | Python |
| **Multimodal LLMs (Local)** | **Meta Muse Glimmer (30B)** / **Qwen2-VL**, Hugging Face `transformers`, `vLLM` |
| **Meta-Learning & Continual Learning** | `learn2learn`, Avalanche (`avalanche-lib`), PEFT/LoRA adapters |
| **Explainability & XAI** | Captum, SHAP, Attention Rollout visualization, LangGraph Tracing |
| **Agent Frameworks** | LangGraph / OpenAI Agents SDK |
| **Agent Interoperability** | Model Context Protocol (MCP) |
| **Optimization Solvers** | Google OR-Tools / Gurobi |
| **Transport Simulation** | SimPy / SUMO / OSMnx / NetworkX |
| **Unified Database & Spatial** | **SurrealDB** (Graph + Spatial + Time-Series + Vectors) *or* PostGIS + pgvector |
| **Backend & Frontend** | FastAPI, Streamlit, Docker Compose |

---

# 🚦 4. The Control Center & Live Dashboard

<div align="center">

![Transportation Digital Twin](images/agentic_control.png)

</div>

The X-ACTDT Control Center is an advanced, real-time multi-agent urban intelligence system powered by **LangGraph**, **Google OR-Tools**, and **SurrealDB**. It monitors regional traffic telemetry, evaluates weather conditions, executes automated policy plans, records continual adaptation metrics, and exposes XAI audit trails to eliminate traffic bottlenecks safely.

## ✨ Key Dashboard Features
* **🤖 Interactive Multi-Agent Workflow Graph:** Visualizes live data packet motion in real time across LangGraph nodes (`Perception`, `ReAct Planner`, `Meta-Adapter`, `OR-Tools Matrix`, `Recovery Handler`, and `XAI Auditor`).
* **🕹️ Flexible Simulation Playback Modes:** Supports single-step inspections or continuous automated multi-step loops (expanding up to 20+ simulation steps).
* **💬 Live Node-to-Directive Mapping & XAI Traces:** Displays real-time agent reasoning text, feature attribution heatmaps, and operator recommendations directly below the workflow graph.
* **🔍 Input Data Deep-Dive Tab:** Allows operators to inspect raw JSON payloads, environmental overrides, and sensor speed distributions to compare *why* and *when* agents trigger recovery protocols.
* **💾 SurrealDB Audit Trail:** Automatically persists execution records, meta-learning adaptation weights, and historical telemetry for post-hoc analysis.

---

# 📚 5. The R&D Roadmap: Journey to X-ACTDT

This curriculum is structured into progressive phases leading directly to the deployment of the capstone system.

## Phase I: Foundations & Multimodal Perception (Modules 1–3)
* Introduction to LLMs, Transformers, Attention Mechanisms, and Context Windows.
* **Vision-Language Models:** Spatial-temporal grounding and processing live traffic camera streams (CCTV) using **Qwen2-VL** and **Meta Muse Glimmer**.
* **Weather & Environmental Perception:** Training agents to detect visibility, precipitation, and adverse surface conditions from video streams.
* Vector indexing, spatial-vector search, and managing multi-model structures via **SurrealDB** or **PostgreSQL + PostGIS + pgvector**.

## Phase II: Agentic Reasoning & Optimization (Modules 4–7)
* **Agentic RAG:** Document loading, chunking, vector indexing, retrieval, context injection, and system-specific retrieval loops for dynamic operational policies.
* **ReAct & Self-Correction Loops:** Reasoning, planning, tool execution, and error handling.
* **Model Context Protocol (MCP):** Exposing real-time digital twin states natively to AI agents.
* **Deterministic Solvers:** Coupling agent decisions with mathematical optimization engines (**Google OR-Tools**) to compute weather-resilient routes.
* **Multi-Agent Orchestration:** Collaboration, role decomposition, task delegation, and consensus mechanisms using **LangGraph**.

## Phase III: Advanced Adaptation & Explainability (Modules 8–11)
* **Advanced MLLM Architectures:** Cross-modal alignment, vision-language projectors, and native tokenization of continuous video feeds and telemetry tensors.
* **Meta-Learning for Rapid Spatial Adaptation:** Utilizing Model-Agnostic Meta-Learning (MAML) and Reptile loops to allow the digital twin to instantly adapt its control logic to unfamiliar layouts.
* **Continual Learning & Mitigating Catastrophic Forgetting:** Managing lifelong urban adaptation across seasonal weather shifts using parameter-efficient continual learning and rehearsal buffers.
* **Multimodal Explainability (XAI):** Unpacking black-box MLLM choices via multimodal attention rollout, integrated gradients, concept bottleneck layers, and causal audit trails.

## Phase IV: Capstone Deployment (Modules 12–13)
* **The Weather-Aware Agentic Transportation Digital Twin:** Integrating traffic simulation engines (**SUMO/SimPy**), spatial databases, and MLLM multi-agent systems into the final production deployment.

## 📈 Learning Progress Tracker

| Lesson | Topic | Status |
| --- | --- | --- |
| 01 | LLMs & Transformer Foundations | ✅ |
| 02 | MLLM Perception (Vision & Weather) | ⏳ |
| 03 | Unified Vector & Spatial Databases | ⏳ |
| 04 | RAG & Agentic RAG | ⏳ |
| 05 | ReAct Agents, Failure Recovery & MCP | ⏳ |
| 06 | MLLMs + Mathematical Solvers (OR-Tools) | ⏳ |
| 07 | Multi-Agent Orchestration (LangGraph) | ⏳ |
| 08 | Advanced MLLM Fine-Tuning & Deployment | ⏳ |
| 09 | Meta-Learning for Rapid Spatial Adaptation | ⏳ |
| 10 | Continual Learning & Mitigating Forgetting | ⏳ |
| 11 | Multimodal Explainability (XAI) & Auditing | ⏳ |
| 12 | Building the Transport Digital Twin (SUMO) | ⏳ |
| 13 | Production Deployment & Monitoring | ⏳ |

---

# 📖 5. References & Academic Foundation

### Foundation Models, MLLMs & Adaptation
* **Attention Is All You Need** (Vaswani et al., 2017).
* **Qwen2-VL: Enhancing Vision-Language Models for SOTA Visual Perception** (Alibaba Group).
* **Muse Glimmer: Open-Weights Multimodal Agentic Models** (Meta).
* **Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks** (Finn et al., 2017).
* **Continual Lifelong Learning with Deep Networks: A Review** (Parisi et al., 2019).

### Explainability, Agentic Frameworks & Digital Twins
* **ReAct: Synergizing Reasoning and Acting in Language Models** (Yao et al., 2022).
* **Model Context Protocol (MCP) Specification** — *Standardized context connectors for AI agents.*
* **LangGraph Documentation** — *Stateful multi-actor application architecture.*
* **A Survey on Explainable Artificial Intelligence (XAI) for Multimodal Systems** (2024–2025).
* **LLM-Powered Digital Twins for Interactive Urban Mobility Simulation** (OpenReview, 2025).

### Transportation & Environmental Spatial Systems
* **SurrealDB Multi-Model Architecture Whitepaper**.
* **OSMnx: New Methods for Complex Street Networks** (Boeing, 2017).
* **Impact of Adverse Weather on Traffic Flow Characteristics** (Transportation Research Board).

---

<div align="center">

# 📈 Contributions & ⭐ Support

Contributions, suggestions, and pull requests are welcome! If you find this R&D repository and the X-ACTDT project helpful, please consider giving it a ⭐.

</div>
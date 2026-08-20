# 🚀 AI, LLM, RAG, MLLMs & Agentic Transportation Digital Twins

Welcome!

This repository documents an end-to-end journey into **Large Language Models (LLMs)**, **Multimodal LLMs (MLLMs)**, **Retrieval-Augmented Generation (RAG)**, **Vector Databases**, and **Agentic AI Systems** applied to complex cyber-physical environments.

Rather than simply reading about these topics, this repository focuses on building state-of-the-art, simulation-backed **Agentic Digital Twins** from the ground up using cutting-edge open and proprietary models.

---

# 🎯 Architecture Diagram

![Technical Architecture: Agentic Transportation Digital Twin](images/architecture.png)

---

# 🎯 Objectives

By completing this repository:

* Master Large Language Models and multi-agent coordination loops.
* Leverage state-of-the-art **Multimodal LLMs** (such as **Qwen2-VL** and Meta's **Muse Glimmer**) to parse live CCTV feeds, maps, and visual telemetry.
* Build autonomous **AI Agents** capable of reasoning, planning, tool-calling, and failure recovery using the **ReAct framework** and **Model Context Protocol (MCP)**.
* Interface MLLMs with deterministic mathematical optimization solvers (e.g., **Google OR-Tools**) for optimal routing.
* Design, simulate, and deploy a production-grade **Transportation Digital Twin** that is **Environment-Aware** (weather, visibility, road conditions).

---

# 📚 Course Roadmap

## Module 1 — Foundations
* Introduction to LLMs, Transformers, Attention Mechanisms, and Context Windows.

## Module 2 — Advanced Multimodal Foundations (MLLMs) & Perception
* Vision-Language Models, spatial-temporal grounding, and processing live traffic camera streams (CCTV) using **Qwen2-VL** and **Meta Muse Glimmer**.
* **Weather & Environmental Perception:** Training agents to detect visibility, precipitation, and adverse surface conditions from video streams.

## Module 3 — Embeddings & Unified Digital Twin Databases
* Vector indexing, spatial-vector search, and managing multi-model structures via **SurrealDB** or **PostgreSQL + PostGIS + pgvector**.

## Module 4 — Retrieval-Augmented Generation (RAG) & Agentic RAG
* Document loading, chunking, vector indexing, retrieval, context injection, and system-specific retrieval loops for dynamic operational policies (e.g., weather response protocols).

## Module 5 — Agentic Architectures & Tool Use
* **ReAct & Self-Correction Loops:** Reasoning, planning, tool execution, and error handling.
* **Model Context Protocol (MCP):** Exposing real-time digital twin states (including weather telemetry) natively to AI agents.
* **Deterministic Solvers:** Coupling agent decisions with mathematical optimization engines (OR-Tools) to compute weather-resilient routes.

## Module 6 — Multi-Agent Orchestration
* Multi-agent collaboration, role decomposition, task delegation, and consensus mechanisms using **LangGraph**.

## Module 7 — Capstone: The Weather-Aware Agentic Transportation Digital Twin
* Integrating traffic simulation engines (SUMO/SimPy), spatial databases, and MLLM multi-agent systems to simulate extreme weather scenarios and real-time disruption responses.

---

# 🧠 Spotlight: SOTA Architecture of the Transportation Digital Twin

The capstone project models a **Generative Agentic Digital Twin** that bridges real-time telemetry with autonomous agentic action:

1. **The Cyber-Physical Environment:** Simulated via **SUMO / SimPy** mimicking real-world intersections, transit lines, and vehicle fleets. Environmental variables (rain, snow, fog) are dynamically applied via the **TraCI** interface.
2. **The Data & Context Layer:** Powered by **SurrealDB** or **PostGIS** for unified spatial, vector, and time-series storage, exposed to agents via the **Model Context Protocol (MCP)**.
3. **The Multi-Agent Team (LangGraph & Local MLLMs):**
   * **Vision & Perception Agent:** Powered by **Muse Glimmer 30B** or **Qwen2-VL**, parsing live CCTV feeds and weather states.
   * **Optimization Agent:** Translates agent insights into mathematical parameters for deterministic solvers (**Google OR-Tools**) to compute routes accounting for reduced capacity/speed.
   * **Disruption Response Agent:** Handles unexpected blockages or severe weather conditions, executing self-correction and failure-recovery protocols.

---

# 🛠 Technology Stack

| Category | SOTA Tools & Frameworks |
| --- | --- |
| Language | Python |
| **Multimodal LLMs (Local)** | **Meta Muse Glimmer (30B)** / **Qwen2-VL** |
| **Agent Frameworks** | LangGraph / OpenAI Agents SDK |
| **Agent Interoperability** | Model Context Protocol (MCP) |
| **Optimization Solvers** | Google OR-Tools / Gurobi |
| **Transport Simulation** | SimPy / SUMO / OSMnx / NetworkX |
| **Unified Database & Spatial** | **SurrealDB** (Graph + Spatial + Time-Series + Vectors) *or* PostGIS + pgvector |
| **Backend & Frontend** | FastAPI, Streamlit, Docker Compose |

---

# 📖 Learning Progress

| Lesson | Topic | Status |
| --- | --- | --- |
| 01 | LLMs & Transformer Foundations | ✅ |
| 02 | MLLM Perception (Vision & Weather) | ⏳ |
| 03 | Unified Vector & Spatial Databases | ⏳ |
| 04 | RAG & Agentic RAG | ⏳ |
| 05 | ReAct Agents, Failure Recovery & MCP | ⏳ |
| 06 | MLLMs + Mathematical Solvers (OR-Tools) | ⏳ |
| 07 | Multi-Agent Orchestration (LangGraph) | ⏳ |
| 08 | Building the Transport Digital Twin (SUMO) | ⏳ |
| 09 | Production Deployment & Monitoring | ⏳ |

---

# 📚 References & Reference Documents

### Foundation Models & MLLMs
* **Attention Is All You Need** (Vaswani et al., 2017).
* **Qwen2-VL: Enhancing Vision-Language Models for SOTA Visual Perception** (Alibaba Group).
* **Muse Glimmer: Open-Weights Multimodal Agentic Models** (Meta).

### Agentic Frameworks, Protocols & Digital Twins
* **ReAct: Synergizing Reasoning and Acting in Language Models** (Yao et al., 2022).
* **Model Context Protocol (MCP) Specification** — *Standardized context connectors for AI agents.*
* **LangGraph Documentation** — *Stateful multi-actor application architecture.*
* **LLM-Powered Digital Twins for Interactive Urban Mobility Simulation** (OpenReview, 2025).
* **GenAI-powered Multi-Agent Paradigm for Smart Urban Mobility** (Xu et al., 2024–2026).

### Transportation & Environmental Spatial Systems
* **SurrealDB Multi-Model Architecture Whitepaper**.
* **OSMnx: New Methods for Complex Street Networks** (Boeing, 2017).
* **Impact of Adverse Weather on Traffic Flow Characteristics** (Transportation Research Board).

---

# 📈 Contributions & ⭐ Support

Contributions, suggestions, and pull requests are welcome! If you find this cutting-edge repository helpful, please consider giving it a ⭐.
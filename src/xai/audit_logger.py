# Causal reasoning and step-by-step rationale generators
"""
src/xai/audit_logger.py
-----------------------
Explainable AI (XAI) auditing and causal reasoning logger. Captures decision pipelines,
generates human-readable rationales, and builds auditable trace logs for digital twin compliance.
"""

import json
import logging
import time
from typing import Dict, Any, List, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("XAI-Auditor")

class XAIAuditLogger:
    """
    Maintains a structured audit trail of agent workflows, pairing raw telemetry and 
    perception outputs with step-by-step causal reasoning trees.
    """
    def __init__(self, session_id: Optional[str] = None):
        self.session_id = session_id or f"session_{int(time.time())}"
        self.audit_trail: List[Dict[str, Any]] = []
        logger.info(f"Initialized XAIAuditLogger for session: {self.session_id}")

    def log_decision_step(
        self,
        node_name: str,
        perception_summary: Dict[str, Any],
        agent_reasoning: str,
        action_taken: str,
        causal_factors: List[str],
        confidence_score: float = 1.0
    ) -> Dict[str, Any]:
        """
        Records a single node execution step in the LangGraph workflow, 
        explicitly documenting the causal relationship between perception and action.
        """
        timestamp = time.time()
        step_record = {
            "session_id": self.session_id,
            "timestamp": timestamp,
            "node": node_name,
            "perception": perception_summary,
            "reasoning": agent_reasoning,
            "action": action_taken,
            "causal_factors": causal_factors,
            "confidence_score": confidence_score,
            "explanation_summary": self._generate_causal_narrative(node_name, causal_factors, action_taken)
        }
        
        self.audit_trail.append(step_record)
        logger.info(f"[XAI Audit] Node '{node_name}' logged successfully. Action: {action_taken}")
        return step_record

    def _generate_causal_narrative(self, node: str, factors: List[str], action: str) -> str:
        """
        Synthesizes a human-readable causal narrative statement explaining 
        the justification behind an agentic directive.
        """
        factors_str = ", ".join(factors) if factors else "standard operational telemetry"
        return (
            f"At node [{node}], the system evaluated conditions ({factors_str}) "
            f"and concluded that executing [{action}] was necessary to maintain network throughput and safety standards."
        )

    def get_full_audit_report(self) -> Dict[str, Any]:
        """
        Returns the complete chronological audit report for post-hoc inspection 
        or regulatory compliance checks.
        """
        return {
            "session_id": self.session_id,
            "total_steps": len(self.audit_trail),
            "trail": self.audit_trail
        }

    def export_audit_json(self, filepath: str) -> None:
        """
        Persists the audit trail to disk in JSON format for database synchronization or UI inspection.
        """
        report = self.get_full_audit_report()
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(report, f, indent=4)
            logger.info(f"Audit trail successfully exported to {filepath}")
        except Exception as e:
            logger.error(f"Failed to export audit log: {e}")
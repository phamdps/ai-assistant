# Model-Agnostic Meta-Learning loops for unseen urban zones
"""
src/meta_learning/maml.py
-------------------------
Model-Agnostic Meta-Learning (MAML) implementation for rapid spatial adaptation 
of traffic policy and routing prediction models across unseen urban topologies.
"""

import logging
from typing import Dict, List, Tuple, Callable, Optional
import torch
import torch.nn as nn
import torch.optim as optim

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MetaLearning-MAML")

class UrbanMAMLAdapter:
    """
    Implements a MAML meta-learning loop designed to rapidly adapt urban traffic 
    control networks to new geographical layouts or unexpected road layout changes 
    using minimal few-shot rollout data.
    """
    def __init__(
        self,
        model: nn.Module,
        inner_lr: float = 0.01,
        meta_lr: float = 0.001,
        num_inner_steps: int = 3,
        device: str = "cpu"
    ):
        self.model = model.to(device)
        self.inner_lr = inner_lr
        self.num_inner_steps = num_inner_steps
        self.device = device
        self.meta_optimizer = optim.Adam(self.model.parameters(), lr=meta_lr)
        
    def clone_parameters(self) -> Dict[str, torch.Tensor]:
        """Creates a detached copy of current model parameters for inner loop tracking."""
        return {name: param.clone() for name, param in self.model.named_parameters()}

    def inner_update(
        self, 
        support_x: torch.Tensor, 
        support_y: torch.Tensor, 
        loss_fn: Callable,
        fast_weights: Optional[Dict[str, torch.Tensor]] = None
    ) -> Dict[str, torch.Tensor]:
        """
        Performs few-shot inner gradient adaptation steps on a specific task 
        (e.g., a specific intersection layout under rain conditions).
        """
        if fast_weights is None:
            fast_weights = self.clone_parameters()

        for step in range(self.num_inner_steps):
            # Forward pass using functional evaluation or parameter override simulation
            # (Simplified explicit parameter update simulation for modular clarity)
            predictions = self._functional_forward(support_x, fast_weights)
            loss = loss_fn(predictions, support_y)
            
            # Compute gradients with respect to fast weights
            grads = torch.autograd.grad(loss, fast_weights.values(), create_graph=True)
            
            # Perform inner gradient descent update step
            fast_weights = {
                name: param - self.inner_lr * grad
                for (name, param), grad in zip(fast_weights.items(), grads)
            }
            
        return fast_weights

    def _functional_forward(
        self, 
        x: torch.Tensor, 
        weights: Dict[str, torch.Tensor]
    ) -> torch.Tensor:
        """
        Executes a forward pass substituting model parameters with fast weights 
        to preserve backpropagation tracking across the meta-gradient loop.
        """
        # In practice, functional execution packages like torch.func (or higher) 
        # manage weight swapping. Here we mock standard forward for structural integration.
        with torch.no_grad():
            original_state = {n: p.clone() for n, p in self.model.named_parameters()}
        
        for name, param in self.model.named_parameters():
            if name in weights:
                param.data.copy_(weights[name])
                
        output = self.model(x)
        
        # Restore original state after functional call
        for name, param in self.model.named_parameters():
            param.data.copy_(original_state[name])
            
        return output

    def meta_train_step(
        self, 
        task_batch: List[Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]], 
        loss_fn: Callable
    ) -> float:
        """
        Executes a full MAML meta-update step across a batch of diverse urban topologies.
        Each task is a tuple of (support_x, support_y, query_x, query_y).
        """
        self.meta_optimizer.zero_grad()
        meta_loss = 0.0

        for support_x, support_y, query_x, query_y in task_batch:
            support_x, support_y = support_x.to(self.device), support_y.to(self.device)
            query_x, query_y = query_x.to(self.device), query_y.to(self.device)

            # 1. Inner loop: Adapt weights on the task support set
            adapted_weights = self.inner_update(support_x, support_y, loss_fn)

            # 2. Outer loop: Evaluate adapted weights on the query set (unseen local state)
            query_preds = self._functional_forward(query_x, adapted_weights)
            task_query_loss = loss_fn(query_preds, query_y)
            
            meta_loss += task_query_loss

        # Average loss across task batch and backpropagate meta-gradients
        meta_loss = meta_loss / len(task_batch)
        meta_loss.backward()
        self.meta_optimizer.step()

        logger.info(f"Meta-training step completed. Outer Meta-Loss: {meta_loss.item():.4f}")
        return meta_loss.item()
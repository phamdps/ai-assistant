import simpy
import random

class TrafficSimulationEngine:
    def __init__(self, env: simpy.Environment):
        self.env = env
        self.queues = {"intersection_A": 45, "intersection_B": 12}

    def run_tick(self):
        while True:
            for node in self.queues:
                self.queues[node] += random.randint(-4, 6)
                if self.queues[node] < 0:
                    self.queues[node] = 0
            print(f"[SimPy Engine @ t={self.env.now}s] Current Intersection Queue Metrics: {self.queues}")
            yield self.env.timeout(3)

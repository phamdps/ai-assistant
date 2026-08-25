"""
Phase 3: Deterministic Optimization Solver Module
Couples MLLM environmental insights with Google OR-Tools for resilient traffic routing.
"""

from ortools.constraint_solver import routing_enums_pb2, pywrapcp

class TrafficOptimizer:
    def __init__(self, base_distance_matrix: list[list[int]], num_vehicles: int = 1, depot: int = 0):
        self.base_matrix = base_distance_matrix
        self.num_vehicles = num_vehicles
        self.depot = depot

    def _create_data_model(self, weather_penalty_multiplier: float = 1.0) -> dict:
        """
        Adjusts the base distance/travel-time matrix using weather penalty factors.
        """
        # Apply weather/congestion penalties dynamically across the matrix
        adjusted_matrix = [
            [int(cell * weather_penalty_multiplier) for cell in row]
            for row in self.base_matrix
        ]
        
        data = {}
        data['distance_matrix'] = adjusted_matrix
        data['num_vehicles'] = self.num_vehicles
        data['depot'] = self.depot
        return data

    def compute_optimal_routes(self, weather_condition: str = "clear") -> dict:
        """
        Solves the Vehicle Routing Problem (VRP) considering weather-induced friction.
        """
        # Determine penalty multiplier based on weather condition
        multipliers = {
            "clear": 1.0,
            "moderate rain": 1.2,
            "heavy rain": 1.4,
            "dense fog": 1.5,
            "snow": 1.7
        }
        multiplier = multipliers.get(weather_condition.lower(), 1.1)
        
        # Instantiate data model with weather-adjusted costs
        data = self._create_data_model(weather_penalty_multiplier=multiplier)

        # Create Routing Index Manager
        manager = pywrapcp.RoutingIndexManager(
            len(data['distance_matrix']), data['num_vehicles'], data['depot']
        )

        # Create Routing Model
        routing = pywrapcp.RoutingModel(manager)

        # Define distance callback
        def distance_callback(from_index, to_index):
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return data['distance_matrix'][from_node][to_node]

        transit_callback_index = routing.RegisterTransitCallback(distance_callback)

        # Define cost of each arc
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        # Add Distance constraint
        dimension_name = 'Distance'
        routing.AddDimension(
            transit_callback_index,
            0,  # no slack
            3000,  # vehicle maximum travel distance per route
            True,  # start cumul to zero
            dimension_name
        )
        distance_dimension = routing.GetDimensionOrDie(dimension_name)
        distance_dimension.SetGlobalSpanCostCoefficient(100)

        # Setting first solution heuristic
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
        )

        # Solve the problem
        solution = routing.SolveWithParameters(search_parameters)

        if solution:
            routes = []
            total_distance = 0
            for vehicle_id in range(data['num_vehicles']):
                index = routing.Start(vehicle_id)
                route = []
                route_distance = 0
                while not routing.IsEnd(index):
                    node_index = manager.IndexToNode(index)
                    route.append(node_index)
                    previous_index = index
                    index = solution.Value(routing.NextVar(index))
                    route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
                route.append(manager.IndexToNode(index))
                routes.append({"vehicle": vehicle_id, "route": route, "cost": route_distance})
                total_distance += route_distance
            
            return {
                "status": "success",
                "weather_condition": weather_condition,
                "applied_multiplier": multiplier,
                "optimized_routes": routes,
                "total_cost": total_distance
            }
        else:
            return {"status": "failed", "reason": "No feasible routing solution found."}

if __name__ == "__main__":
    # Test stub with a sample 4-node network matrix
    sample_matrix = [
        [0, 548, 776, 696],
        [548, 0, 684, 308],
        [776, 684, 0, 992],
        [696, 308, 992, 0]
    ]
    optimizer = TrafficOptimizer(sample_matrix, num_vehicles=2, depot=0)
    result = optimizer.compute_optimal_routes(weather_condition="heavy rain")
    print(result)
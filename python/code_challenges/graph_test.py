from data_structures.queue import Queue

class Node:
    def __init__(self, value=None):
        self.value = value


class Edge:
    def __init__(self, value_a, value_b, weight):
        self.origin = value_a
        self.destination = value_b
        self.weight = weight


class Graph:
    def __init__(self):
        self.nodes = list()
        self.edges = list()
        self.node_names = list()

    def __str__(self):
        node_list = list()
        for node in self.nodes:
            node_list.append(node.value)
        return str(node_list)

    def add_node(self, value):
        if value in self.node_names:
            raise Exception
            return
        else:
            self.nodes.append(Node(value))
            self.node_names.append(value)

    def add_edge(self, value_a, value_b, weight):
        if value_a not in self.node_names or value_b not in self.node_names:
            raise Exception
            return
        else:
            # loop thru edges to match origin and destination.  If found, update weight
            for edge in self.edges:
                if edge.origin == value_a and edge.destination == value_b:
                    edge.weight = weight
                    return
            # not in list of edges: add edge
            self.edges.append(Edge(value_a, value_b, weight))

    def travel_cost(self, origin, destination):
        travel_cost_dict = dict()
        valid_routes = self.valid_routes(origin, destination)
        route_cost_list = list()

        # Find the cost of each route
        for route in valid_routes:
            route_cost_list.append(self.route_cost(route))

        # Find index of lowest cost
        lowest_cost = float('inf')
        lowest_index = None
        for idx, route_cost in enumerate(route_cost_list):
            if route_cost < lowest_cost:
                lowest_cost = route_cost
                lowest_index = idx

        print(f'Lowest cost route: {valid_routes[lowest_index]}')
        print(f'Cost: {route_cost_list[lowest_index]}')

    def valid_routes(self, origin, destination):
        # Return a list of all possible valid routes from origin to destination
        valid_routes = list()
        current_route = list()

        def route_finder(graph, origin, destination, current_route=[]):
            nonlocal valid_routes
            current_route.append(origin)

            for edge in graph.edges:
                # Add edges to queue
                if edge.origin == origin and edge.destination not in current_route:
                    # Destination found
                    if edge.destination == destination:
                        current_route.append(edge.destination)
                        valid_routes.append(current_route)
                        return
                    else:
                        # Key here is the current_route[:].  shallow copy
                        route_finder(graph, edge.destination, destination, current_route[:])

        route_finder(self, origin, destination, current_route)

        return valid_routes

    def route_cost(self, route):
        current_cost = 0

        for stop_num in range(len(route) - 1):
            first_stop = route[stop_num]
            second_stop = route[stop_num + 1]

            # Find edge
            for edge in self.edges:
                if edge.origin == first_stop and edge.destination == second_stop:
                    current_cost += edge.weight
        return current_cost

    def route_to_string(self, route):
        route_name = ''
        for stop in route:
            route_name = route_name + str(stop) + ' -> '
        route_name = route_name[:-4]
        return route_name

graph = Graph()
graph.add_node('a')
graph.add_node('b')
graph.add_node('c')
graph.add_node('d')
graph.add_node('e')

graph.add_edge('a', 'b', 1)
graph.add_edge('a', 'd', 9)
graph.add_edge('b', 'c', 3)
graph.add_edge('c', 'd', 4)
graph.add_edge('d', 'a', 9)
graph.add_edge('d', 'e', 5)

# graph.travel_cost('b', 'a')
graph.travel_cost('b', 'd')


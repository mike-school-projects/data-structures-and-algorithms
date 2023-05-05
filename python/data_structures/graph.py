class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        self.node_dict = dict()

    def __str__(self):
        return str(self.get_nodes())

    def add_node(self, value):
        node = Vertex(value)
        self.node_dict[node] = list()

        return node

    def add_edge(self, node1, node2, weight=0):
        # Check to see if nodes are in the graph
        if (node1 not in self.node_dict.keys()) or (node2 not in self.node_dict.keys()):
            raise KeyError

        self.node_dict[node1].append(Edge(node2, weight))
        # Check to see if edge is looped back to itself
        if node1 == node2:
            return
        self.node_dict[node2].append(Edge(node1, weight))

    def get_nodes(self):
        return self.node_dict.keys()

    def get_neighbors(self, node):
        return self.node_dict[node]

    def size(self):
        return len(self.node_dict.keys())


class Vertex:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Edge:
    def __init__(self, node, weight=0):
        self.vertex = node
        self.weight = weight


if __name__ == "__main__":
    graph = Graph()
    banana = graph.add_node("banana")
    apple = graph.add_node("apple")
    loner = Vertex("loner")
    actual = len(graph.get_nodes())
    print(actual)



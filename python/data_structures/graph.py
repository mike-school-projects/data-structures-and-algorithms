from data_structures.queue import Queue

class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        self.node_list = list()

    def __str__(self):
        return str(self.get_nodes())

    def add_node(self, value):
        node = Vertex(value)
        self.node_list.append([node, []])

        return node

    def add_edge(self, node1, node2, weight=0):
        # Check to see if nodes are in the graph
        node_names = self.get_nodes()

        if (node1 not in node_names) or (node2 not in node_names):
            raise KeyError

        for node in self.node_list:
            if node1 == node[0]:
                node[1].append(Edge(node2, weight))

    def get_nodes(self):
        output_nodes = list()
        for node in self.node_list:
            output_nodes.append(node[0])
        return output_nodes

    def get_neighbors(self, input_node):
        output_list = list()
        for node in self.node_list:
            if input_node == node[0]:
                output_list = node[1]
        return output_list

    def size(self):
        return len(self.node_list)

    def breadth_first(self, node):
        # keep track of which vertexes have already been listed
        output_list_of_vertexes = list()

        # Use queue for breadth-first search
        vertex_queue = Queue()

        vertex_queue.enqueue(node)

        while vertex_queue.is_empty() is False:
            current_vertex = vertex_queue.dequeue()

            # Check to see if current has already been listed
            if current_vertex not in output_list_of_vertexes:
                # Add to output list
                output_list_of_vertexes.append(current_vertex)

                # Add vertexes to queue
                edge_list = self.get_neighbors(current_vertex)
                for edge in edge_list:
                    if edge.vertex not in output_list_of_vertexes:
                        vertex_queue.enqueue(edge.vertex)


        neighbor_names = list()
        for vertex in output_list_of_vertexes:
            neighbor_names.append(vertex.value)

        return neighbor_names

    def depth_first_search(self, node, visited=list()):
        # Already in node list, stop recursion
        if node.value in visited:
            return visited

        # Add this node to visited list
        list_of_nodes = list()
        for node_edge_pair in self.node_list:
            list_of_nodes.append(node_edge_pair[0].value)

        # Check if node is in graph
        if node.value not in list_of_nodes:
            return visited

        # Add to visited
        visited.append(node.value)

        # Get list of edges
        edge_list = self.get_neighbors(node)

        # recursive call
        for edge in edge_list:
            if edge.vertex.value not in visited:
                visited = self.depth_first_search(edge.vertex)

        return visited



class Vertex:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Edge:
    def __init__(self, node, weight=0):
        self.vertex = node
        self.weight = weight


def graph_and_root():
    letters = Graph()

    a = letters.add_node("a")
    b = letters.add_node("b")
    c = letters.add_node("c")
    d = letters.add_node("d")
    e = letters.add_node("e")
    f = letters.add_node("f")
    g = letters.add_node("g")
    h = letters.add_node("h")

    letters.add_edge(a, b)
    letters.add_edge(b, c)
    letters.add_edge(c, g)
    letters.add_edge(a, d)

    letters.add_edge(d, e)
    letters.add_edge(d, h)
    letters.add_edge(d, f)

    letters.add_edge(h, f)


    return letters


if __name__ == "__main__":

    graph = Graph()
    root = Vertex("some other node")
    print(graph.depth_first_search(root))





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

    realms = Graph()

    pandora = realms.add_node("Pandora")
    arendelle = realms.add_node("Arendelle")
    metroville = realms.add_node("Metroville")
    monstropolis = realms.add_node("Monstropolis")
    narnia = realms.add_node("Narnia")
    naboo = realms.add_node("Naboo")

    realms.add_edge(pandora, arendelle)

    realms.add_edge(arendelle, pandora)
    realms.add_edge(arendelle, metroville)
    realms.add_edge(arendelle, monstropolis)

    realms.add_edge(metroville, arendelle)
    realms.add_edge(metroville, monstropolis)
    realms.add_edge(metroville, narnia)

    realms.add_edge(monstropolis, arendelle)
    realms.add_edge(monstropolis, metroville)
    realms.add_edge(monstropolis, naboo)

    realms.add_edge(narnia, metroville)
    realms.add_edge(narnia, naboo)

    realms.add_edge(naboo, metroville)
    realms.add_edge(naboo, monstropolis)
    realms.add_edge(naboo, narnia)


    nodes = realms.get_nodes()
    edges = realms.get_neighbors(naboo)
    for edge in edges:
        print(edge.vertex.value)




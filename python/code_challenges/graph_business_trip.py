from data_structures.graph import Graph

def direct_flights(graph, itinerary_list):
    total_cost = 0
    start_location_vertex = ''
    end_location_vertex = ''

    # Loop through list of destinations starting with index 0 as start point, up to 2nd from last
    for index in range(len(itinerary_list)-1):
        start_location_name = itinerary_list[index]
        end_location_name = itinerary_list[index + 1]

        # convert to vertexs
        for location in graph.node_list:
            if location[0].value == start_location_name:
                start_location_vertex = location[0]

            if location[0].value == end_location_name:
                end_location_vertex = location[0]

        # Find edges
        start_edges = graph.get_neighbors(start_location_vertex)

        # Check for valid segment
        valid_segment = False
        for edge in start_edges:
            if edge.vertex == end_location_vertex:
                total_cost += edge.weight
                valid_segment = True

        if valid_segment is False:
            return None

    return total_cost

def planets():
    graph = Graph()

    metroville = graph.add_node("Metroville")
    pandora = graph.add_node("Pandora")
    arendelle = graph.add_node("Arendelle")
    new_monstropolis = graph.add_node("New Monstropolis")
    naboo = graph.add_node("Naboo")
    narnia = graph.add_node("Narnia")

    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(arendelle, pandora, 150)

    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(metroville, pandora, 82)

    graph.add_edge(metroville, arendelle, 99)
    graph.add_edge(arendelle, metroville, 99)

    graph.add_edge(new_monstropolis, arendelle, 42)
    graph.add_edge(arendelle, new_monstropolis, 42)

    graph.add_edge(new_monstropolis, metroville, 105)
    graph.add_edge(metroville, new_monstropolis, 105)

    graph.add_edge(new_monstropolis, naboo, 73)
    graph.add_edge(naboo, new_monstropolis, 73)

    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(naboo, metroville, 26)

    graph.add_edge(metroville, narnia, 37)
    graph.add_edge(narnia, metroville, 37)

    graph.add_edge(narnia, naboo, 250)
    graph.add_edge(naboo, narnia, 250)

    return graph

if __name__ == "__main__":
    graph = planets()
    names = ["Pandora", "Arendelle", "Metroville", "Naboo"]
    print(direct_flights(graph, names))



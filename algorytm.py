from bellman_ford import bellman_ford
       
def transform_object(obj):
    graph = {}
    for node in obj:
        name = node['name']
        neighbors = [(neighbor, weight) for neighbor, weight in node['neighbors'].items()]
        graph[name] = neighbors
    return graph

def msg_window(graph, start_node, end_node):
    if len(graph) == 0:
        return ["Graf jest pusty",[]]
    shortest_path = bellman_ford(graph, start_node, end_node)
    if shortest_path[1] == float('-inf'):
        tekst = f"Ujemny cykl istnieje {shortest_path[0]}"
        shortest_path[0].append(shortest_path[0][0])
        return [tekst, shortest_path[0][::-1]]
    if shortest_path[1] == float('inf'):
        return [f"Nie ma połączenia między {start_node} i {end_node}", []]
    else:
        total_distance = shortest_path[1]
        return [f"Najkrótsza droga z {start_node} do {end_node}: {shortest_path[0]}" + "\n" + f"Całkowita odległość: {total_distance}",shortest_path[0]]

from bellman_ford import bellman_ford
from dijkstra import dijkstra
from has_negative_weight import has_negative_weight

# Przykładowy graf
graph = {
    'A': [('B', 5), ('C', 2)],
    'B': [('D', 1), ('E', 6)],
    'C': [('B', 1), ('D', 2)],
    'D': [('E', 1)],
    'E': [],
    'F':[]
}
graph6 = {
    'A': [('E', 2)],
    'B': [('A', 1), ('C', 1)],
    'C': [('D', 3)],
    'D': [('E', -1)],
    'E': [('B', -2)],
    'F': [('A', -4),('E', -1)],
    'G': [('F', 1)],
    'S': [('A', 10),('G', 8)],
}
start_node = 'A'
end_node = 'E'

def msg(start_node, end_node, shortest_path, total_distance):
    """
    Prints the shortest path and total distance between two nodes.

    Args:
        start_node (str): The starting node.
        end_node (str): The ending node.
        shortest_path (list): The list of nodes representing the shortest path.
        total_distance (float): The total distance of the shortest path.

    Returns:
        None
    """
    if total_distance == float('inf'):
        print(f"Nie ma połączenia między {start_node} i {end_node}")
    else:
        print(f"Najkrótsza droga z {start_node} do {end_node}: {shortest_path}")
        print(f"Całkowita odległość: {total_distance}")
    

def algorytm(graph, start_node, end_node):
    """
    Finds the shortest path in a graph from a start node to an end node.

    Args:
        graph (dict): The graph represented as a dictionary of nodes and their neighbors.
        start_node: The starting node.
        end_node: The target node.

    Returns:
        None

    Prints:
        - If the graph is empty: "Graf jest pusty"
        - If there is a negative cycle: "Ujemny cykl istnieje"
        - If there is a shortest path: The shortest path from start_node to end_node and its total distance.
    """
    if len(graph) == 0:
        print("Graf jest pusty")
        return
    if has_negative_weight(graph):
        shortest_path = bellman_ford(graph, start_node, end_node)
        if shortest_path is None:
            print("Ujemny cykl istnieje")
        else:
            total_distance = shortest_path[1]
            msg(start_node, end_node, shortest_path[0], total_distance)
    else:
        shortest_path, total_distance = dijkstra(graph, start_node, end_node)
        msg(start_node, end_node, shortest_path, total_distance)

algorytm(graph, start_node, end_node)
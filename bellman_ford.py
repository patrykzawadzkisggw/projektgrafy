def bellman_ford(graph, start, end):
    """
    Implementuje algorytm Bellmana-Forda do znajdywania najkrótszej drogi między dwoma wierzchołkami w grafie.

    :param graph: Graf w postaci listy sąsiedztwa z wagami krawędzi.
    :param start: Punkt początkowy.
    :param end: Punkt końcowy.
    :return: Krotka zawierająca najkrótszą drogę i jej długość, lub None jeśli istnieje ujemny cykl.
    """
    if len(graph) == 0:
        return None
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                distance = distances[node] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = node

    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                return None  # Ujemny cykl istnieje

    path = []
    current_node = end

    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous[current_node]

    return path, distances[end]
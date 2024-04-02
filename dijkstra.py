def dijkstra(graph, start, end):
    """
    Implementuje algorytm Dijkstry do znajdywania najkrótszej drogi między dwoma wierzchołkami w grafie.

    :param graph: Graf w postaci listy sąsiedztwa z wagami krawędzi.
    :param start: Punkt początkowy.
    :param end: Punkt końcowy.
    :return: Krotka zawierająca najkrótszą drogę i jej długość.
    """
    if len(graph) == 0:
        return None
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}

    queue = [(start, 0)]

    while queue:
        current_node, current_distance = queue.pop(0)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                queue.append((neighbor, distance))

    path = []
    current_node = end

    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous[current_node]

    return path, distances[end]
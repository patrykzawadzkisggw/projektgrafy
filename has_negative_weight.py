def has_negative_weight(graph):
    """
    Sprawdza, czy w grafie skierowanym istnieje wierzchołek o ujemnej wadze.

    :param graph: Graf w postaci listy sąsiedztwa z wagami wierzchołków.
    :return: True, jeśli istnieje wierzchołek o ujemnej wadze, False w przeciwnym razie.
    """
    for node in graph:
        for _, weight in graph[node]:
            if weight < 0:
                return True
    return False
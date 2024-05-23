def bellman_ford(graph, start, end):
    if len(graph) == 0:
        return None

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}

    for _ in range(len(graph) - 1):
        changed = False
        for node in graph:
            for neighbor, weight in graph[node]:
                distance = distances[node] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = node
                    changed = True
        if not changed:
            break

    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]: # A negative cycle exists
                ncycle = [node]
                node = previous[node]
                while node != ncycle[0]:
                    ncycle.append(node)
                    node = previous[node]
                return ncycle,float('-inf')  

    path = []
    current_node = end

    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous[current_node]

    return path, distances[end]

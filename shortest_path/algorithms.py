import heapq


def dijkstra(graph, start, end=None):

    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)
        

        if end is not None and current_node == end:
            return distances[end]
            
        if current_dist > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node]:
            if distances[current_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_node] + weight
                heapq.heappush(heap, (distances[neighbor], neighbor))
    

    return distances[end] if end is not None else distances


def bellman_ford(graph, start, end=None):

    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    

    for _ in range(n - 1):
        for u in range(n):
            for v, weight in graph[u]:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    

    for u in range(n):
        for v, weight in graph[u]:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                return "Negative cycle detected"

    return distances[end] if end is not None else distances


def floyd_warshall(graph, start=None, end=None):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0
        for j, weight in graph[i]:
            dist[i][j] = weight
    

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    

    if start is not None and end is not None:
        return dist[start][end]
    return dist

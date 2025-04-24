import heapq


def dijkstra(graph, start): #O((V + E) log V)
    n = len(graph)  # O(1)
    distances = [float('inf')] * n  # O(n)
    distances[start] = 0  # O(1)
    heap = [(0, start)]  # O(1)

    while heap:  # O((V + E) log V)
        current_dist, current_node = heapq.heappop(heap)  # O(log V)
        if current_dist > distances[current_node]:  # O(1)
            continue
        for neighbor, weight in graph[current_node]:  # O(E)
            if distances[current_node] + weight < distances[neighbor]:  # O(1)
                distances[neighbor] = distances[current_node] + weight  # O(1)
                heapq.heappush(heap, (distances[neighbor], neighbor))  # O(log V)
    return distances


def bellman_ford(graph, start): #O(V*E)
    n = len(graph)  # O(1)
    distances = [float('inf')] * n  # O(V)
    distances[start] = 0  # O(1)
    for _ in range(n - 1):  # O(V)
        for u in range(n):  # O(V)
            for (v, weight) in graph[u]:  # O(E)
                if distances[u] + weight < distances[v]:  # O(1)
                    distances[v] = distances[u] + weight  # O(1)
    has_negative_cycle = False  # O(1)
    for u in range(n):  # O(V)
        for (v, weight) in graph[u]:  # O(E)
            if distances[u] + weight < distances[v]:  # O(1)
                has_negative_cycle = True  # O(1)
                break  # O(1)
        if has_negative_cycle:  # O(1)
            break  # O(1)

    if has_negative_cycle:  # O(1)
        return "Negative cycle detected"  # O(1)
    else:
        return distances  # O(1)
def floyd_warshall(graph): #O(n³)
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]  # O(n²)
    for i in range(n):  # O(n)
        dist[i][i] = 0  # O(1)
        for (j, weight) in graph[i]:
            if weight < dist[i][j]:  # O(1)
                dist[i][j] = weight  # O(1)

    for k in range(n):  # O(n³)
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


import random
from collections import deque

def get_random_graph(size, limit=100, ensure_path=True):

    if size == 0:
        return [[], -1, -1, 0]


    graph = [[] for _ in range(size)]
    edge_count = 0


    for i in range(size):

        num_edges = random.randint(0, max(1, size // 2))
        target_nodes = set()


        for _ in range(num_edges):
            target = random.randint(0, size - 1)
            if target != i:
                target_nodes.add(target)


        for target in target_nodes:
            weight = random.randint(1, limit)
            graph[i].append((target, weight))
            edge_count += 1


    start = random.randint(0, size - 1)
    goal = random.randint(0, size - 1)
    

    while start == goal and size > 1:
        goal = random.randint(0, size - 1)


    if ensure_path and not has_path(graph, start, goal):
        add_path(graph, start, goal, limit)
        edge_count += 1

    return [graph, start, goal, edge_count]


def add_path(graph, start, end, limit):

    if start == end:
        return


    n = len(graph)
    intermediate_nodes = list(set(range(n)) - {start, end})
    random.shuffle(intermediate_nodes)
    

    path_nodes = [start]
    if n > 2 and random.random() < 0.5:
        num_intermediates = random.randint(1, min(3, len(intermediate_nodes)))
        path_nodes.extend(intermediate_nodes[:num_intermediates])
    path_nodes.append(end)
    

    for i in range(len(path_nodes) - 1):
        u = path_nodes[i]
        v = path_nodes[i + 1]

        existing_edge = False
        for idx, (target, _) in enumerate(graph[u]):
            if target == v:
                existing_edge = True
                break
                

        if not existing_edge:
            weight = random.randint(1, limit)
            graph[u].append((v, weight))


def has_path(graph, start, goal):

    if start == goal:
        return True

    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
            
        visited.add(node)
        
        for neighbor, _ in graph[node]:
            if neighbor == goal:
                return True
            if neighbor not in visited:
                queue.append(neighbor)

    return False

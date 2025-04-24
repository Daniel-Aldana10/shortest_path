import random
from collections import deque

def get_random_graph(size, limit=100, ensure_path=True):
    if size == 0:
        return [[], -1, -1, 0]

    answer = [[] for _ in range(size)]
    m = 0

    for i in range(size):
        num_relations = random.randint(0, max(1, size // 2))
        relations = set()

        for _ in range(num_relations):
            vert = random.randint(0, size - 1)
            if vert != i:
                relations.add(vert)

        for elem in relations:
            weight = random.randint(1, limit)
            answer[i].append([elem, weight])
            m += 1

    start = random.randint(0, size - 1)
    goal = random.randint(0, size - 1)
    while start == goal and size > 1:
        goal = random.randint(0, size - 1)

    if ensure_path and not has_path(answer, start, goal):
        add_path(answer, start, goal, limit)
        m += 1

    return [answer, start, goal, m]


def add_path(adj_list, start, end, limit):
    if start == end:
        return

    intermediate_nodes = list(set(range(len(adj_list))) - {start, end})
    random.shuffle(intermediate_nodes)

    forced_path = [start] + intermediate_nodes[:max(0, len(adj_list) - 2)] + [end]

    for i in range(len(forced_path) - 1):
        u = forced_path[i]
        v = forced_path[i + 1]
        if v not in [n for n, _ in adj_list[u]]:
            weight = random.randint(1, limit)
            adj_list[u].append([v, weight])


def has_path(graph, start, goal):
    if start == goal:
        return True

    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor, _ in graph[node]:
            if neighbor == goal:
                return True
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False

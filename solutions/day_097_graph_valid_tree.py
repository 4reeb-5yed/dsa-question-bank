from collections import defaultdict, deque

def valid_tree(n, edges):
    if len(edges) != n - 1:
        return False
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    visited = set()
    queue = deque([0])
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    return len(visited) == n
from collections import deque

def shortest_distance(grid):
    if not grid or not grid[0]:
        return -1
    m, n = len(grid), len(grid[0])
    dist = [[0] * n for _ in range(m)]
    reach = [[0] * n for _ in range(m)]
    buildings = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                buildings += 1
                bfs(grid, i, j, dist, reach, m, n)

    if buildings == 0:
        return -1
    result = float('inf')
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0 and reach[i][j] == buildings:
                result = min(result, dist[i][j])
    return result if result != float('inf') else -1

def bfs(grid, i, j, dist, reach, m, n):
    visited = [[False] * n for _ in range(m)]
    queue = deque([(i, j, 0)])
    visited[i][j] = True
    while queue:
        x, y, d = queue.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                if grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    dist[nx][ny] += d + 1
                    reach[nx][ny] += 1
                    queue.append((nx, ny, d + 1))
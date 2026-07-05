from collections import deque

def update_matrix(mat):
    if not mat:
        return mat
    m, n = len(mat), len(mat[0])
    result = [[float('inf')] * n for _ in range(m)]
    queue = deque()
    # Only add ORIGINALLY zero cells to the queue
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                result[i][j] = 0
                queue.append((i, j))
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    while queue:
        i, j = queue.popleft()
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and result[ni][nj] == float('inf'):
                # Only update cells that haven't been visited yet
                result[ni][nj] = result[i][j] + 1
                queue.append((ni, nj))
    return [[int(result[i][j]) if result[i][j] != float('inf') else -1 for j in range(n)] for i in range(m)]
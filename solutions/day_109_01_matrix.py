from collections import deque

def update_matrix(mat):
    if not mat:
        return mat
    m, n = len(mat), len(mat[0])
    result = [[float('inf')] * n for _ in range(m)]
    queue = deque()
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
            if 0 <= ni < m and 0 <= nj < n:
                if result[ni][nj] > result[i][j] + 1:
                    result[ni][nj] = result[i][j] + 1
                    queue.append((ni, nj))
    # Replace inf with a large number or keep as is
    return result
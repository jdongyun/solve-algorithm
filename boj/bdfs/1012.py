from collections import deque
directions = [(-1,0), (0, 1), (1, 0), (0, -1)]
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    cabbages = [[False] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        i, j = map(int, input().split())
        cabbages[i][j] = True
    queue = deque()
    size = 0
    for i in range(n):
        for j in range(m):
            queue.append((i, j))
            count = 0
            while queue:
                x, y = queue.popleft()
                if not cabbages[x][y] or visited[x][y]:
                    continue
                visited[x][y] = True
                count += 1
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if cabbages[nx][ny]:
                            queue.append((nx, ny))
            if count > 0:
                size += 1
    print(size)

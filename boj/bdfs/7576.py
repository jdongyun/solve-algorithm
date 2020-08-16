from collections import deque
m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

visited = [[False] * m for _ in range(n)]
queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))
count = 0
while queue:
    x, y = queue.popleft()
    visited[x][y] = True
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and box[nx][ny] == 0:
                queue.append((nx, ny))
                box[nx][ny] = box[x][y] + 1
                count = max(count, box[nx][ny])
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit(0)
print(max(count - 1, 0))

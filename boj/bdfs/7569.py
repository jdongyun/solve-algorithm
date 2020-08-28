from collections import deque
m, n, h = map(int, input().split())
graph = [[] for _ in range(h)]
for z in range(h):
    for x in range(n):
        graph[z].append(list(map(int, input().split())))

notriped = []
visited = [[[-1] * m for _ in range(n)] for _ in range(h)]
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                notriped.append((i, j, k))
                visited[i][j][k] = 1

directions = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]

q = deque(notriped)
while q:
    x, y, z = q.popleft()
    for dx, dy, dz in directions:
        nx, ny, nz = x + dx, y + dy, z + dz
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
            if visited[nx][ny][nz] == -1 and graph[nx][ny][nz] == 0:
                visited[nx][ny][nz] = visited[x][y][z] + 1
                q.append((nx, ny, nz))
count = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] != -1 and visited[i][j][k] == -1:
                print(-1)
                exit(0)
            if visited[i][j][k] > count:
                count = visited[i][j][k]
print(count - 1)

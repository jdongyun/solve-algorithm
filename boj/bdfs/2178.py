from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

dist = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dist[0][0] = 1
visited[0][0] = True

queue = deque([(0, 0)])
while queue:
    x, y = queue.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 1 and not visited[nx][ny]:
                dist[nx][ny] = dist[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))

print(dist[n-1][m-1])

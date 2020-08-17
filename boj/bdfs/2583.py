from collections import deque

m, n, k = map(int, input().split())
board = [[False] * (m) for _ in range(n)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            board[x][y] = True
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
result = []
for i in range(n):
    for j in range(m):
        if board[i][j]:
            continue
        queue = deque([(i, j)])
        board[i][j] = True
        count = 0
        while queue:
            x, y = queue.popleft()
            count += 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not board[nx][ny]:
                        board[nx][ny] = True
                        queue.append((nx, ny))
        if count > 0:
            result.append(count)
print(len(result))
result.sort()
print(' '.join(map(str, result)))

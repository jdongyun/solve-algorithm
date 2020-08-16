from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ranges = set()
for i in range(n):
    for j in range(n):
        ranges.add(board[i][j])

def bfs(under):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            flag = False
            if board[i][j] <= under or visited[i][j]:
                continue
            queue = deque([(i, j)])
            visited[i][j] = True
            while queue:
                x, y = queue.popleft()
                flag = True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] > under and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
            if flag:
                count += 1
    return count

max_count = 1
for i in ranges:
    max_count = max(max_count, bfs(i))
print(max_count)

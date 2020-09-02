import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip() 
r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
d = [[int(1e9)] * c for _ in range(r)]
q = deque()

# 물부터 큐에 넣어서 물 먼저 처리하도록 함
for i in range(r):
    for j in range(c):
        if board[i][j] == '*':
            q.append(('*', i, j))
for i in range(r):
    for j in range(c):
        if board[i][j] == 'S':
            q.append((0, i, j))

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
while q:
    t, x, y = q.popleft() 
    # 큐에 물 먼저 넣어두었으므로 물을 다 처리할 때까지 반복함
    while q and (t == '*'):
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] == '.':
                    q.append(('*', nx, ny))
                    board[nx][ny] = '*'
        t, x, y = q.popleft() 
    
    if board[x][y] == '*':
        continue
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            if board[nx][ny] == '.':
                q.append((t + 1, nx, ny))
                board[nx][ny] = t+1
            elif board[nx][ny] == 'D':
                print(t + 1)
                exit(0)
print('KAKTUS')

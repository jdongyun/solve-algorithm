import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip() 
n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(m)]
d = [[int(1e9)] * 100 for _ in range(100)]
d[0][0] = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
q = deque([(0, 0)])
while q:
    i, j = q.popleft()
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < m and 0 <= nj < n:
            if board[ni][nj] == 1 and d[ni][nj] > d[i][j] + 1:
                q.append((ni, nj))
                d[ni][nj] = d[i][j] + 1
            elif board[ni][nj] == 0 and d[ni][nj] > d[i][j]:
                q.append((ni, nj))
                d[ni][nj] = d[i][j]
                
print(d[m-1][n-1])

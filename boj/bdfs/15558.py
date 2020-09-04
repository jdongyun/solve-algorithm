import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
n, k = map(int, input().split())
board = [list(map(int, input())) for _ in range(2)]
q = deque([(0, 0, 0)])
visited = [[False] * (n + k + 1) for _ in range(2)]
while q:
    t, lr, i = q.popleft()
    for ni in [i-1, i+1]:
        if 0 <= ni <= n+k and t < ni:
            if ni >= n: 
                print(1)
                exit(0)
            if board[lr][ni] == 1 and not visited[lr][ni]:
                visited[lr][ni] = True
                q.append((t + 1, lr, ni))
    nlr = 1 - lr
    ni = i + k
    if 0 <= ni <= n+k and t < ni:
        if ni >= n: 
            print(1)
            exit(0)
        if board[nlr][ni] == 1 and not visited[nlr][ni]:
            visited[nlr][ni] = True
            q.append((t + 1, nlr, ni))
print(0)

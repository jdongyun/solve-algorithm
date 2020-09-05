import sys
sys.setrecursionlimit(10000)
from collections import deque
input = lambda: sys.stdin.readline().rstrip() 

def check(board):
    if board == '123456780':
        return True
    return False

board = ''
for _ in range(3):
    a, b, c = list(map(str, input().split()))
    board += a + b + c

zero = -1
for i in range(9):
    if board[i] == '0':
        zero = i
        break
visited = set()
visited.add(board)

q = deque([(zero, board, 0)])
while q:
    i, b, c = q.popleft()
    if check(b):
        print(c)
        exit(0)
    for ni in [i-3, i+3]:
        mini = min(i, ni)
        maxi = max(i, ni)
        if 0 <= ni < 9:
            nb = b[0:mini] + b[maxi] + b[mini+1:maxi] + b[mini] + b[maxi+1:]
            if nb not in visited:
                q.append((ni, nb, c+1))
                visited.add(nb)
    for ni in [i-1, i+1]:
        mini = min(i, ni)
        maxi = max(i, ni)
        if (i//3)*3 <= ni < (i//3) * 3 + 3:
            nb = b[0:mini] + b[maxi] + b[mini+1:maxi] + b[mini] + b[maxi+1:]
            if nb not in visited:
                q.append((ni, nb, c+1))
                visited.add(nb)
print(-1)

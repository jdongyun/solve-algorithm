import sys
import heapq
from collections import deque
from itertools import combinations, permutations
input = lambda: sys.stdin.readline().rstrip() 

test = True
if test:
    sys.stdin = open('input.txt', 'r')
    print('sys.stdin = input.txt')

def dest(board, i, j, dx, dy):
    while True:
        if board[i+dx][j+dy] == 'O':
            return i+dx, j+dy
        if board[i+dx][j+dy] == '#':
            return i, j
        i += dx
        j += dy
    return -1, -1

def distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
bx, by = 0, 0
rx, ry = 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'B':
            bx, by = i, j
            board[i][j] = '.'
        elif board[i][j] == 'R':
            rx, ry = i, j
            board[i][j] = '.'

directions = [(0, -1, 0), (1, 1, 0), (2, 0, 1), (3, 0, -1)]
q = deque()
q.append((bx, by, rx, ry, '4')) # 4는 directions의 di에 겹치지 않기 위한 더미
while q:
    bx, by, rx, ry, c = q.popleft()
    if board[rx][ry] == 'O':
        print(len(c) - 1)
        exit(0)
    if len(c) > 10:
        continue

    last_c = int(c[-1])
    for di, dx, dy in directions:
        if di == last_c:
            continue
        nbx, nby = dest(board, bx, by, dx, dy)
        nrx, nry = dest(board, rx, ry, dx, dy)
        if (nbx, nby) == (nrx, nry):
            if board[nbx][nby] == 'O': # 둘이 같은 위치로 되었다면 둘 다 구멍에 빠진 것으로 됨
                continue
            if distance(nbx, nby, bx, by) > distance(nbx, nby, rx, ry): # 현위치에서 누가 더 먼가(= 누가 한 칸 옆에 있을 것인가)
                nbx, nby = nbx - dx, nby - dy
            else:
                nrx, nry = nrx - dx, nry - dy
        if board[nbx][nby] == 'O' and board[nrx][nry] != 'O': # 파란 공만 빠졌을 경우 큐에 넣지 않음
            continue
        q.append((nbx, nby, nrx, nry, c + str(di)))
print(-1)

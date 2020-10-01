from collections import deque
from copy import deepcopy
import heapq
from itertools import combinations, permutations
from itertools import combinations_with_replacement
import sys

input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(100000)

test = True
if test:
    try:
        sys.stdin = open('input_data.txt', 'r')
        print('sys.stdin = input.txt')
    except FileNotFoundError:
        pass

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

r, c, tm = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
air_fresher = []
for i in range(r):
    for j in range(c):
        if board[i][j] == -1:
            air_fresher.append((i, j))

def circulate(board, init_x, init_y, t, direction):
    if t == 0:
        x, y = init_x - 1, init_y
    else:
        x, y = init_x + 1, init_y
    for d in direction:
        while True:
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy
            if t == 0 and not (0 <= nx < init_x + 1 and 0 <= ny < c):
                break
            if t == 1 and not(init_x <= nx < r and 0 <= ny < c):
                break
            if nx == init_x and ny == init_y:
                break
            board[x][y] = board[nx][ny]
            x, y = nx, ny
    board[init_x][init_y + 1] = 0

def move_dust(board, r, c):
    coord = []
    for x in range(r):
        for y in range(c):
            if board[x][y] >= 1:
                coord.append((x, y, board[x][y] // 5))
    for x, y, diffusion in coord:
        cnt = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] != -1:
                    cnt += 1
        board[x][y] -= (diffusion) * cnt
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] != -1:
                    board[nx][ny] += diffusion

for _ in range(tm):
    move_dust(board, r, c)
    circulate(board, *air_fresher[0],0, [0, 1, 2, 3])
    circulate(board, *air_fresher[1],1, [2, 1, 0, 3])

s = 0
for i in range(r):
    for j in range(c):
        if board[i][j] != -1:
            s += board[i][j]
print(s)
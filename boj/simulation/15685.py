import sys
import heapq
from collections import deque
from itertools import combinations, permutations, combinations_with_replacement
from copy import deepcopy
input = lambda: sys.stdin.readline().rstrip() 

test = True
if test:
    try:
        sys.stdin = open('input_data.txt', 'r')
        print('sys.stdin = input.txt')
    except FileNotFoundError:
        pass
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
def generation(limit, d):
    ret = [d]
    i = 1
    while i <= limit:
        for j in range(len(ret) - 1, -1, -1):
            nd = ret[j]
            ret.append(((nd - 2) % 4 - 1) % 4)
        i += 1
    return ret

board = [[0] * 101 for _ in range(101)]
n = int(input())
curves = [list(map(int, input().split())) for _ in range(n)]
for y, x, d, g in curves:
    gen = generation(g, d)
    board[x][y] = 1
    nx, ny = x, y
    for nd in gen:
        dx, dy = directions[nd]
        nx, ny = nx + dx, ny + dy
        board[nx][ny] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i+1][j+1] == 1:
            cnt += 1
print(cnt)
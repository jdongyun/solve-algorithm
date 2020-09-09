import sys
import heapq
from collections import deque
from itertools import combinations, permutations
from copy import deepcopy
input = lambda: sys.stdin.readline().rstrip() 

test = True
if test:
    sys.stdin = open('input.txt', 'r')
    print('sys.stdin = input.txt')
tetro = [
    ["####"],
    ["##",
     "##"],
    ["# ",
     "# ",
     "##"],
    ["# ",
     "##",
     " #"],
    ["###",
     " # "]
]
def rotate_90_degree(arr):
    row_len, col_len = len(arr), len(arr[0])
    ret = [[0] * row_len for _ in range(col_len)]
    for i in range(col_len):
        for j in range(row_len):
            ret[i][j] = arr[row_len - j - 1][i]
    return ret
tetros = []
for t in tetro:
    arr = deepcopy(t)
    
    for _ in range(4):
        arr = rotate_90_degree(arr)
        d = []
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == '#':
                    d.append((i, j))
        tetros.append(d)
    arr = arr[::-1]
    for _ in range(4):
        arr = rotate_90_degree(arr)
        d = []
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == '#':
                    d.append((i, j))
        tetros.append(d)
                    
n, m = map(int, input().split())
board = []
for i in range(4):
    board.append([0] * (m + 8))
for _ in range(n):
    board.append([0] * 4 + list(map(int, input().split())) + [0] * 4)
for i in range(4):
    board.append([0] * (m + 8))
max_value = 0
for tet in tetros:
    for i in range(4, 4+n):
        for j in range(4, 4+m):
            tmp = 0
            for dx, dy in tet:
                nx, ny = i + dx, j + dy
                tmp += board[nx][ny]
            max_value = max(max_value, tmp)
print(max_value )

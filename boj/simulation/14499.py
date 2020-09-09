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

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cmds = list(map(int, input().split()))

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
d = [0] * 6
def get_dice_bottom():
    return d[2]
def set_dice_bottom(i):
    global d
    d[2] = i
def get_dice_top():
    return d[5]
def set_dice_top(i):
    global d
    d[5] = i
def next_dice(dx, dy):
    global d
    if dx == 0 and dy == 1: #right
        d = [d[0], d[2], d[3], d[5], d[4], d[1]]
    if dx == 0 and dy == -1: #left
        d = [d[0], d[5], d[1], d[2], d[4], d[3]]
    if dx == 1 and dy == 0: #down
        d = [d[2], d[1], d[4], d[3], d[5], d[0]]
    if dx == -1 and dy == 0: #up
        d = [d[5], d[1], d[0], d[3], d[2], d[4]]

for cmd in cmds:
    dx, dy = directions[cmd-1]
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < m:
        next_dice(dx, dy)
        if board[nx][ny] == 0:
            board[nx][ny] = get_dice_bottom()
        else:
            set_dice_bottom(board[nx][ny])
            board[nx][ny] = 0
        print(get_dice_top())
        x, y = nx, ny

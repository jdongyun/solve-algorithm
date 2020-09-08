import sys
import heapq
from collections import deque
from itertools import combinations, permutations
input = lambda: sys.stdin.readline().rstrip() 

test = True
if test:
    sys.stdin = open('input.txt', 'r')
    print('sys.stdin = input.txt')
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
board = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        board[i][j] = l[i][j] + l[j][i]
min_value = int(1e9)
for combination in combinations(range(n), n // 2):
    i1 = 0
    for c1, c2 in combinations(combination, 2):
        x, y = min(c1, c2), max(c1, c2)
        i1 += board[x][y]
    i2 = 0
    for c1, c2 in combinations(list(set(range(n)) - set(combination)), 2):
        x, y = min(c1, c2), max(c1, c2)
        i2 += board[x][y]
    min_value = min(min_value, abs(i1 - i2))
print(min_value)

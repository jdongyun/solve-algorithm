import bisect
from collections import deque
from copy import deepcopy
import decimal
import heapq
from itertools import combinations, permutations
from itertools import combinations_with_replacement
import sys
import math
from sys import modules

sys.setrecursionlimit(100_000)
input = lambda: sys.stdin.readline().rstrip() 
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

test = True
if test:
    try:
        sys.stdin = open('input_data.txt', 'r')
        print('sys.stdin = input.txt')
    except FileNotFoundError:
        pass

directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

n, fm, k = map(int, input().split())
q = deque()
for _ in range(fm):
    r, c, m, s, d = map(int, input().split())
    q.append((r-1, c-1, m, s, d))

for _ in range(k):
    arr = [[[] for _ in range(n)] for _ in range(n)]
    for _ in range(len(q)):
        r, c, m, s, d = q.popleft()
        nr, nc = r + (directions[d][0] * s), c + (directions[d][1] * s)
        nr, nc = nr % n, nc % n
        arr[nr][nc].append((m, s, d))
    
    for i in range(n):
        for j in range(n):
            if len(arr[i][j]) == 1:
                q.append((i, j, *arr[i][j][0]))
            elif len(arr[i][j]) > 1:
                m = sum(x[0] for x in arr[i][j]) // 5
                if m == 0: continue

                s = sum(x[1] for x in arr[i][j]) // len(arr[i][j])

                cnt = sum(1 if x[2] % 2 == 0 else -1 for x in arr[i][j])
                if abs(cnt) == len(arr[i][j]):
                    start = 0
                else:
                    start = 1
                for d in range(start, 8, 2):
                    q.append((i, j, m, s, d))

print(sum(x[2] for x in q))
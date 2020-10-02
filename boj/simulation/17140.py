from collections import deque
from copy import deepcopy
import heapq
from itertools import combinations, permutations
from itertools import combinations_with_replacement
import sys

input = lambda: sys.stdin.readline().rstrip() 
test = True
if test:
    try:
        sys.stdin = open('input_data.txt', 'r')
        print('sys.stdin = input.txt')
    except FileNotFoundError:
        pass

rr, cc, k = map(int, input().split())
board = [[0] * 100 for _ in range(100)]
for i in range(3):
    a = list(map(int, input().split()))
    for j in range(3):
        board[i][j] = a[j]

r, c = 3, 3
for t in range(101):
    if board[rr - 1][cc - 1] == k:
        print(t)
        exit(0)
    
    if r >= c:
        nc = 0
        for i in range(r):
            cnt = [0] * 101
            for j in range(c):
                cnt[board[i][j]] += 1
            tmp = []
            for j in range(1, 101):
                if cnt[j] > 0:
                    tmp.append((j, cnt[j]))
            
            tmp.sort(key=lambda x: x[0])
            tmp.sort(key=lambda x: x[1])
            ret = []
            for x, y in tmp:
                ret.append(x)
                ret.append(y)
            board[i] = ret + ([0] * (100 - len(ret)))
            nc = max(nc, len(ret))
        c = nc
    else:
        nr = 0
        for j in range(c):
            cnt = [0] * 101
            for i in range(r):
                if board[i][j] < 0: break
                cnt[board[i][j]] += 1
            tmp = []
            for i in range(1, 101):
                if cnt[i] > 0:
                    tmp.append((i, cnt[i]))
            tmp.sort(key=lambda x: x[0])
            tmp.sort(key=lambda x: x[1])
            ret = []
            for x, y in tmp:
                ret.append(x)
                ret.append(y)
            nr = max(nr, len(ret))
            for i in range(100):
                if i < len(ret):
                    board[i][j] = ret[i]
                else:
                    board[i][j] = 0
        r = nr

print(-1)

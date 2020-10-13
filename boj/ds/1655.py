from collections import deque
from copy import deepcopy
import decimal
import heapq
from itertools import combinations, permutations
from itertools import combinations_with_replacement
import sys
import math

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

n = int(input())
lq, rq = [], []
for length in range(1, n+1):
    i = int(input())
    heapq.heappush(lq, (-i, i))
    while len(lq) > len(rq):
        j = heapq.heappop(lq)[1]
        heapq.heappush(rq, j)
    while len(lq) < len(rq):
        j = heapq.heappop(rq)
        heapq.heappush(lq, (-j, j))
    print(lq[0][1])
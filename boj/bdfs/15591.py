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

n, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, r = map(int, input().split())
    graph[a].append((b, r))
    graph[b].append((a, r))

for _ in range(q):
    k, v = map(int, input().split())
    cnt = 0
    visited = [False] * (n + 1)
    visited[v] = True
    q = deque([v])
    while q:
        i = q.popleft()
        for j, r in graph[i]:
            if not visited[j]:
                if r >= k:
                    visited[j] = True
                    cnt += 1
                    q.append(j)
    print(cnt)

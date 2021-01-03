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

for _ in range(int(input())):
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    max_times = [0] * (n + 1)
    for _ in range(k):
        i, j = map(int, input().split())
        graph[i].append(j)
        indegree[j] += 1

    w = int(input())
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        i = q.popleft()
        for j in graph[i]:
            indegree[j] -= 1
            max_times[j] = max(max_times[j], max_times[i] + d[i])
            if indegree[j] == 0:
                q.append(j)
    print(max_times[w] + d[w])

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
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j, d = map(int, input().split())
    graph[i].append((j, d))
start, end = map(int, input().split())

def dijkstra(graph, start, n):
    distance = [int(1e9)] * (n + 1)
    q = [(0, start)]
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for j, d in graph[now]:
            cost = dist + d
            if cost < distance[j]:
                distance[j] = cost
                heapq.heappush(q, (cost, j))
    return distance

distance = dijkstra(graph, start, n)
print(distance[end])
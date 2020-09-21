import sys
sys.setrecursionlimit(100000)
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

v = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(v):
    t = list(map(int, input().split()))
    p = t[0]
    for i in range(1, len(t) - 1, 2):
        j, l = t[i], t[i+1]
        graph[p].append((j, l))

def dfs(i, w):
    global max_i, max_value, visited
    if w > max_value:
        max_i = i
        max_value = w
    for j, nw in graph[i]:
        if not visited[j]:
            visited[j] = True
            dfs(j, w + nw)

visited = [False] * (v + 1)
visited[1] = True
max_i = -1
max_value = 0
dfs(1, 0)

visited = [False] * (v + 1)
visited[max_i] = True
max_value = 0
dfs(max_i, 0)

print(max_value)

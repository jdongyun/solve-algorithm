import sys
import heapq
from collections import deque
from itertools import combinations, permutations
from copy import deepcopy
input = lambda: sys.stdin.readline().rstrip() 

test = True
if test:
    try:
        sys.stdin = open('input_data.txt', 'r')
        print('sys.stdin = input.txt')
    except FileNotFoundError:
        pass

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
for c in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][c] + graph[c][j] < graph[i][j]:
                graph[i][j] = graph[i][c] + graph[c][j]
length = int(1e9)
ran = list(range(k)) + list(range(k + 1, n))
for permutation in permutations(ran, n-1):
    min_len = 0
    start = k
    for p in permutation:
        min_len += graph[start][p]
        start = p
    length = min(min_len, length)

print(length)

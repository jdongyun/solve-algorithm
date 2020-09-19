import sys
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

n = int(input())
tree = {}
for _ in range(n - 1):
    a, b = map(int, input().split())
    if a not in tree:
        tree[a] = [b]
    else:
        tree[a].append(b)
    if b not in tree:
        tree[b] = [a]
    else:
        tree[b].append(a)

parent = [0] * 100_001
q = deque()
q.append(1)
while q:
    i = q.popleft()
    for j in tree[i]:
        if parent[j] == 0:
            q.append(j)
            parent[j] = i

for i in range(2, n + 1):
    print(parent[i])

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

def loc(l):
    ret = 0
    for i in l:
        ret = i + ret * 60
    return ret

n = int(input())
power = list(map(int, input().split()))
visited = [False] * (61 * 61 * 61)
q = deque()
q.append((0, power[:]))
while q:
    cnt, p = q.popleft()
    if sum(p) == 0:
        print(cnt)
        break
    for per in permutations([9, 3, 1][:n], n):
        np = [max(p[i] - per[i], 0) for i in range(n)]
        print(np)
        if not visited[loc(np)]:
            visited[loc(np)] = True
            q.append((cnt + 1, np))
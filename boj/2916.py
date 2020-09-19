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

n, k = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
check = [False] * 360
q = deque()
q.append((0, a1[0]))
while q:
    idx, res = q.popleft()
    check[res] = True

    for nres in [res + res, res + a1[idx], abs(res - a1[idx])]:
        nres = nres % 360
        if not check[nres]:
            check[nres] = True
            q.append((idx, nres))

    if idx == n - 1: continue
    for nres in [abs(res + a1[idx + 1]), abs(res - a1[idx + 1])]:
        nres = nres % 360
        if idx + 1 < n and not check[nres]:
            q.append((idx + 1, nres))
            check[nres] = True
for a in a2:
    if check[a]:
        print('YES')
    else:
        print('NO')

# https://www.acmicpc.net/problem/15684
import sys
import heapq
from collections import deque
from itertools import combinations, permutations, combinations_with_replacement
from copy import deepcopy
input = lambda: sys.stdin.readline().rstrip() 

test = False
if test:
    try:
        sys.stdin = open('input_data.txt', 'r')
        print('sys.stdin = input.txt')
    except FileNotFoundError:
        pass

n, m, height = map(int, input().split())
info = [[False] * (height + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    info[b][a] = True

def end(x):
    for i in range(1, height + 1):
        if info[x][i]:
            x += 1
        elif info[x-1][i]:
            x -= 1
    return x

def can_set(d, h):
    return not info[d-1][h] and not info[d][h] and not info[d+1][h]

def set_bar(d, h, b):
    info[d][h] = b

def check():
    for i in range(1, n+1):
        if end(i) != i:
            return False
    return True

cand = []
for i in range(1, n):
    for j in range(1, height + 1):
        if can_set(i, j):
            cand.append((i, j))
            
result = -1
def run():
    global result
    if check():
        result = 0
        return
    for cnt in range(1, 4):
        if len(cand) < cnt:
            return
        for combination in combinations(cand, cnt):
            ok_count = 0
            for c in combination:
                if not can_set(*c):
                    break
                ok_count += 1
            if ok_count < cnt: continue
            for c in combination:
                set_bar(*c, True)
            if check():
                result = cnt
                return
            for c in combination:
                set_bar(*c, False)
run()
print(result)




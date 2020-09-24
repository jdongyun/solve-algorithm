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

n = int(input())
roots = [True] * (n + 1)
root = 0
tree = {}
for _ in range(n):
    i, a, b = map(int, input().split())
    tree[i] = (a, b)
    if a > 0: roots[a] = False
    if b > 0: roots[b] = False

#root 구하기
for i in range(1, n+1):
    if roots[i]:
        root = i
        break

levels = [([int(1e9)] + [0]) for _ in range(10_001)] #min, max default
count = 0
def inorder(level, i):
    global levels, count
    if tree[i][0] > 0:
        inorder(level + 1, tree[i][0])
    count += 1
    levels[level][0] = min(levels[level][0], count)
    levels[level][1] = max(levels[level][1], count)
    if tree[i][1] > 0:
        inorder(level + 1, tree[i][1])

inorder(1, root)
lev = 1
result = 1
for i in range(1, 10_001):
    if levels[i][1] >= levels[i][0] and \
        levels[i][1] - levels[i][0] + 1 > result:
        result = levels[i][1] - levels[i][0] + 1
        lev = i
print(lev, result)
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
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
points.sort(key=lambda x: x[0])

def dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def solve(points, start, end):
    if end - start + 1 == 2:
        return dist(points[start], points[end])
    if end - start + 1 == 3:
        return min(dist(points[start], points[start + 1]),
                    dist(points[start + 1], points[start + 2]),
                    dist(points[start], points[start + 2]))

    mid = (start + end) // 2
    left = solve(points, start, mid)
    right = solve(points, mid+1, end)
    d = min(left, right)

    mid_x = (points[mid+1][0] + points[mid][0]) // 2
    temp = []
    for i in range(start, end+1):
        if (points[i][0] - mid_x)**2 < d:
            temp.append(points[i])
    temp.sort(key=lambda x: x[1])

    for a in range(len(temp)-1):
        for b in range(a + 1, len(temp)):
            if (temp[b][1]-temp[a][1])**2 >= d: break
            d = min(d, dist(temp[a], temp[b]))
    return d

print(solve(points, 0, n-1))
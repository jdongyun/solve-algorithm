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
grade = [[0] * 6 for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    grade[i][a] = grade[i][b] = 1

result = [0, 0]
for i in range(1, 6):
    max_count = 0
    now_count = 0
    for j in range(n):
        if grade[j][i] > 0:
            now_count += grade[j][i]
        else:
            max_count = max(max_count, now_count)
            now_count = 0
    max_count = max(max_count, now_count)
    if result[0] < max_count:
        result = [max_count, i]
print(*result)

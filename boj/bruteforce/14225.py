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
num = list(map(int, input().split()))
num.sort()
s = [False] * (100_001 * 20)
for cnt in range(1,n + 1):
    for combination in combinations(num, cnt):
        s[sum(combination)] = True
for i in range(1, len(s)):
    if not s[i]:
        print(i)
        break

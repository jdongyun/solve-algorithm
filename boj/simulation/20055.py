import bisect
from collections import deque
from copy import deepcopy
import decimal
import heapq
from itertools import combinations, permutations
from itertools import combinations_with_replacement
import sys
import math
from sys import modules

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

n, k = map(int, input().split())
arr = list(map(int, input().split()))
robots = [False] * n
for step in range(1, 100_000_000):
    # 1. 벨트가 한 칸 회전한다.
    arr = [arr[-1]] + arr[:-1]
    robots = [False] + robots[:-1]
    robots[-1] = False
    
    # 2. 가장 먼저 벨트에 올라간 애부터 한 칸 이동
    for i in range(n-2, -1, -1):
        if arr[i+1] >= 1 and robots[i] and not robots[i+1]:
            robots[i] = False
            robots[i+1] = True
            arr[i+1] -= 1
    
    # 3. 로봇 없으면 로봇 올리기
    if arr[0] >= 1:
        robots[0] = True
        arr[0] -= 1
    
    # 4. 내구도 확인
    zero_cnt = 0
    for a in arr:
        if a == 0:
            zero_cnt += 1
    if zero_cnt >= k:
        print(step)
        exit(0)
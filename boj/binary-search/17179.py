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

n, m, l = map(int, input().split())
cutline = [int(input()) for _ in range(m)]
cutcount = [int(input()) for _ in range(n)]

for cut in cutcount:
    start = 0
    end = l
    max_len = 0
    while start <= end:
        mid = (start + end) // 2
        s = 0
        cnt = 0
        for i in cutline:
            if i - s >= mid:
                s = i
                cnt += 1
        if cnt == cut and l-s < mid:
            end = mid - 1
        elif cnt >= cut:
            max_len = max(max_len, mid)
            start = mid + 1
        else:
            end = mid - 1
    print(max_len)

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
for _ in range(int(input())):
    n = int(input())
    arr = []
    for _ in range(n):
        num = input()
        arr.append(num)
    arr.sort()
    f = False
    for i in range(n-1):
        a, b = arr[i], arr[i+1]
        flag = True
        for j in range(min(len(a), len(b))):
            if a[j] != b[j]:
                flag = False
        if flag:
            f = True
            break
    print('NO' if flag else 'YES')

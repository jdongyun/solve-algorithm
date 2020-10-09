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

def rotate(a, d):
    if d == 1: d = 7
    else: d = 1
    ret = (a * 2)[d:d+8]
    return ret

arr = [list(map(int, list(input()))) for _ in range(4)]
k = int(input())
for _ in range(k):
    i, d = map(int, input().split())
    i -= 1
    new_arr = deepcopy(arr)

    dd = d
    for j in range(i, 0, -1): #왼쪽
        dd *= -1
        if arr[j][6] != arr[j-1][2]:
            new_arr[j-1] = rotate(new_arr[j-1], dd)
        else:
            break
    dd = d
    for j in range(i, 3):
        dd *= -1
        if arr[j][2] != arr[j+1][6]:
            new_arr[j+1] = rotate(new_arr[j+1], dd)
        else:
            break
    arr = new_arr
    arr[i] = rotate(arr[i], d)
    
result = 0
for i in range(4):
    result += (arr[i][0]) << i
print(result)
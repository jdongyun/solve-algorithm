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
plus = [[], [], [], []]
plus[1] = ['1+1+1', '1+2', '2+1', '3']
plus[2] = ['1+1','2']
plus[3] = ['1']

if n < 4:
    if k <= len(plus[4-n]):
        print(plus[4-n][k-1])
    else:
        print(-1)
    exit(0)


for i in range(n-3):
    for j in range(len(plus[1])):
        plus[0].append('1+' + plus[1][j])
    for j in range(len(plus[2])):
        plus[0].append('2+' + plus[2][j])
    for j in range(len(plus[3])):
        plus[0].append('3+' + plus[3][j])
    plus[3] = plus[2]
    plus[2] = plus[1]
    plus[1] = plus[0]
    plus[0] = []
    plus[1].sort()
if k <= len(plus[1]):
    print(plus[1][k-1])
else:
    print(-1)

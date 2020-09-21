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
preorder = []
for line in sys.stdin:
    preorder.append(int(line))

def pre_to_post(preorder):
    leng = len(preorder)
    root = preorder[0]
    over_root = 0
    for i in range(leng):
        if root > preorder[i]:
            over_root = i
    if over_root != 0:
        pre_to_post(preorder[1:over_root+1])
    if over_root != leng - 1:
        pre_to_post(preorder[over_root+1:])
    print(root)
pre_to_post(preorder)

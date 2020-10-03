from collections import deque
from copy import deepcopy
import heapq
from itertools import combinations, permutations
from itertools import combinations_with_replacement
import sys
sys.setrecursionlimit(100_000)
input = lambda: sys.stdin.readline().rstrip() 
test = True
if test:
    try:
        sys.stdin = open('input_data.txt', 'r')
        print('sys.stdin = input.txt')
    except FileNotFoundError:
        pass

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
def postorder_to_preorder(i_s, i_e, p_s, p_e):
    if i_s > i_e or p_s > p_e: return

    root = inorder.index(postorder[p_e])
    print(postorder[p_e], end=' ')
    
    plen = root - i_s

    postorder_to_preorder(i_s, root - 1, p_s, p_s + plen - 1)
    postorder_to_preorder(root + 1, i_e, p_s + plen, p_e - 1)

postorder_to_preorder(0, n - 1, 0, n - 1)
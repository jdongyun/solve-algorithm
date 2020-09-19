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

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.key)

n = int(input())
tree = [Node(0) for _ in range(n)]
for _ in range(n):
    k, l, r = input().split()
    i = ord(k) - ord('A')
    tree[i].key = k
    if l != '.':
        tree[i].left = ord(l) - ord('A')
    if r != '.':
        tree[i].right = ord(r) - ord('A')
def preorder(i):
    print(tree[i].key, end='')
    if tree[i].left != None:
        preorder(tree[i].left)
    if tree[i].right != None:
        preorder(tree[i].right)
preorder(0)
print()

def inorder(i):
    if tree[i].left != None:
        inorder(tree[i].left)
    print(tree[i].key, end='')
    if tree[i].right != None:
        inorder(tree[i].right)
inorder(0)
print()

def postorder(i):
    if tree[i].left != None:
        postorder(tree[i].left)
    if tree[i].right != None:
        postorder(tree[i].right)
    print(tree[i].key, end='')
postorder(0)
print()

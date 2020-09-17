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

def readable(word, letters):
    for i in range(len(word)):
        if word[i] not in letters:
            return False
    return True
    
n, k = map(int, input().split())
words = [list(input())[4:-4] for _ in range(n)]
antic = list('antic')
if k < 5:
    print(0)
    exit(0)

s = set()
for word in words:
    for w in word:
        if w not in antic:
            s.add(w)

ret = 0
for combination in combinations(s, min(len(s), k - 5)):
    cnt = 0
    for word in words:
        if readable(word, list(combination) + antic):
            cnt += 1
    ret = max(ret, cnt)
print(ret)

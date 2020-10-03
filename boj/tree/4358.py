from collections import deque
from copy import deepcopy
import decimal
import heapq
from itertools import combinations, permutations
from itertools import combinations_with_replacement
import sys

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

dictionary = {}
count = 0
for line in sys.stdin:
    name = line.rstrip()
    if name in dictionary:
        dictionary[name] += 1
    else:
        dictionary[name] = 1
    count += 1

ret = sorted(dictionary.items())
for k, v in ret:
    print(k, end=' ')
    value = str(v / count * 100)
    d = decimal.Decimal(value)
    print(round(d, 4))
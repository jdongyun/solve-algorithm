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

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n, m = map(int, input().split())
if n % m == 0:
    print(0)
    exit(0)

x, y = n // gcd(n, m), m // gcd(n, m)
count = 0
while x // y < n:
    if x % y != 0:
        count += 1
    x += n // gcd(n, m)
print(count)
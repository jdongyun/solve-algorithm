import sys
from collections import deque
from itertools import permutations
input = lambda: sys.stdin.readline().rstrip()

def next_num(num, d, btns):
    if sum(btns) == 0:
        return -int(1e9)
    while 0 < num <= 999_999:
        num = num + d
        flag = True
        for i in str(num):
            if not btns[int(i)]:
                flag = False
                break
        if flag:
            return num
    return -int(1e9)

n = int(input())
m = int(input())
btns = [True] * 10
if m > 0:
    for i in list(map(int, input().split())):
        btns[i] = False

d = -1 if n < 100 else 1
n1 = next_num(100, d, btns)
n2 = -int(1e9)
while abs(n - n1) < abs(n - n2):
    n2 = n1
    n1 = next_num(n1, d, btns)

cand1 = len(str(n2)) + abs(n - n2)
cand2 = len(str(n1)) + abs(n - n1)
cand3 = abs(n - 100)
print(min(cand1, cand2, cand3))

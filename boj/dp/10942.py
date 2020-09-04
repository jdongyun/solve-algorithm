import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
nums = list(map(int, input().split()))
m = int(input())
ques = [list(map(int, input().split())) for _ in range(m)]
check_odd = [0 for _ in range(2001)]
check_even = [0 for _ in range(2001)]
for i in range(n):
    max_cnt = (-1, -1)
    for j in range(n):
        if i-j < 0 or i+j >= n:
            break
        if nums[i-j] == nums[i+j]:
            max_cnt = (i-j, i+j)
        else:
            break
    check_odd[i] = max_cnt

for i in range(n):
    max_cnt = (-1, -1)
    for j in range(n):
        if i-j < 0 or i+1+j >= n:
            break
        if nums[i-j] == nums[i+1+j]:
            max_cnt = (i-j, i+1+j)
        else:
            break
    check_even[i] = max_cnt

for i, j in ques:
    i, j = i-1, j-1
    if (j - i + 1) % 2 == 0:
        if check_even[(i + j) // 2][0] <= i and check_even[(i + j) // 2][1] >= j:
            print(1)
        else:
            print(0)
    else:
        if check_odd[(i + j) // 2][0] <= i and check_odd[(i + j) // 2][1] >= j:
            print(1)
        else:
            print(0)

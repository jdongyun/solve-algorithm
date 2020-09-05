import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip() 

n = int(input())
num = list(map(int, input().split()))
cnt = [[0] * 21 for _ in range(n-1)] # cnt[i][j] 는 num[0..i]까지의 +- 연산을 모두 더한 카운트
cnt[0][num[0]] = 1
for i in range(1, n-1):
    for j in range(0, 21):
        nc = j - num[i]
        if 0 <= nc <= 20 and cnt[i-1][j] > 0:
            cnt[i][nc] += cnt[i-1][j]
        nc = j + num[i]
        if 0 <= nc <= 20 and cnt[i-1][j] > 0:
            cnt[i][nc] += cnt[i-1][j]
print(cnt[n-2][num[n-1]])

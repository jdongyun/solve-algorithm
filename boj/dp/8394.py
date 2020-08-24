import sys
input = sys.stdin.readline
n = int(input())
d = [0] * 10_000_001
d[0] = 1
d[1] = 1
d[2] = 2
for i in range(3, n+1):
    d[i] = (d[i-1] % 10 + d[i-2] % 10) % 10
print(d[n])

import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
p = [0] + list(map(int, input().split()))
d = [int(1e9)] * (n + 1)
for i in range(1, n + 1):
    min_value = p[i]
    for j in range(1, i+1):
        if i % j == 0:
            min_value = min(min_value, p[j] * (i // j))
        min_value = min(min_value, d[i-j] + d[j])
    d[i] = min_value
print(d[n])

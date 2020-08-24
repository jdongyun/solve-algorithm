import sys
import decimal
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

input = sys.stdin.readline
n = int(input())
arr = [float(input()) for _ in range(n)]
max_value = -1e9
d = [0.0] * n
d[0] = arr[0]

for i in range(1, n):
    d[i] = max(d[i-1] * arr[i], arr[i])
    max_value = max(max_value, d[i])
print(round(decimal.Decimal(str(max_value)), 3))

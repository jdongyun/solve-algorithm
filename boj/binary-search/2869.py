import sys
a, b, v = map(int, sys.stdin.readline().rstrip().split())
start = 0
end = v // (a-b)
result = 1e9
while start <= end:
    mid = (start + end) // 2
    if (a - b) * mid + a >= v:
        end = mid - 1
        result = min(result, mid)
    else:
        start = mid + 1
print(result + 1)

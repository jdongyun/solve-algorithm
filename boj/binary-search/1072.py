x, y = map(int, input().split())
z = int(y * 100 / x)

start = 0
end = 10_000_000_000
result = -1
while start <= end:
    mid = (start + end) // 2
    nz = int((y + mid) * 100 / (mid +x)) # 새로운 승률 계산
    if nz > z:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)

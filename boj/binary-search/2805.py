n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

result = 0
while start <= end:
    mid = (start + end) // 2
    sum_heights = 0
    for t in trees:
        if t > mid:
            sum_heights += t - mid
    if sum_heights >= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)

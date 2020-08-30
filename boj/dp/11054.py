n = int(input())
arr = list(map(int, input().split()))
cache = [[0] * 2 for _ in range(n)]
for i in range(n):
    for j in range(i+1):
        if arr[j] < arr[i]:
            cache[i][0] = max(cache[i][0], cache[j][0] + 1)
for i in range(n-1, -1, -1):
    for j in range(i, n):
        if arr[i] > arr[j]:
            cache[i][1] = max(cache[i][1], cache[j][1] + 1)
max_value = 0
for i in range(n):
    max_value = max(max_value, cache[i][0] + cache[i][1])
print(max_value + 1)

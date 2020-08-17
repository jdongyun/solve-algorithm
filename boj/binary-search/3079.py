n, m = map(int, input().split())
times = []
for _ in range(n):
    times.append(int(input()))
times.sort()

start = 0
end = max(times) * m
result = 0
while start <= end:
    time_limit = (start + end) // 2
    count = 0
    for t in times:
        count += time_limit // t
    if count >= m:
        end = time_limit - 1
        result = time_limit
    else:
        start = time_limit + 1
print(result)

n, m = map(int, input().split())
lessons = list(map(int, input().split()))
if n == m:
    print(max(lessons))
    exit(0)
pSum = [0] * (n+1)
for i in range(1, n+1):
    pSum[i] = lessons[i-1] + pSum[i-1]

start = 0
end = 100_000_000_0
result = 0
while start <= end:
    mid = (start + end) // 2
    count = 1
    j = 0
    for i in range(n):
        if lessons[i] > mid: # 레슨 하나의 길이가 블루레이보다 길면 불가능
            count = -1
            break
        p = pSum[i+1] - pSum[j]
        if p > mid:
            count += 1
            j = i
    if -1 < count <= m:
        end = mid - 1
        result = mid
    else:
        start = mid + 1
    
print(result)

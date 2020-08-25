n = int(input())
arr = list(map(int, input().split()))
d = [0] * n # d[i]는 arr[i]를 끝으로 한 가장 큰 증가하는 부분 수열
d[0] = arr[0]
for i in range(1, n):
    max_value = arr[i] # arr[0:i-1] > arr[i]일 경우
    for j in range(i):
        if arr[j] < arr[i]:
            max_value = max(max_value, d[j] + arr[i])
    d[i] = max_value
print(max(d))

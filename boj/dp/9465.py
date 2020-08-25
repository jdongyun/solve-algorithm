t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    max_value = 0
    for _ in range(2):
        arr.append(list(map(int, input().split())))
    d = [[0] * n for _ in range(2)]
    d[0][0] = arr[0][0]
    d[1][0] = arr[1][0]
    for i in range(1, n):
        d[0][i] = max(d[1][i-1], d[1][i-2]) + arr[0][i]
        d[1][i] = max(d[0][i-1], d[0][i-2]) + arr[1][i]
    print(max(d[0][n-1], d[1][n-1]))

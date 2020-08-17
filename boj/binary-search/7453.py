import bisect
n = int(input())
data = [list(map(int,input().split())) for i in range(n)]
transposed = list(zip(*data))
ab = [transposed[0][i] + transposed[1][j] for i in range(n) for j in range(n)]
cd = [transposed[2][i] + transposed[3][j] for i in range(n) for j in range(n)]
cd.sort()

result = 0
length = len(ab)
for i in ab:
    res = bisect.bisect_right(cd, -i, 0, length) - bisect.bisect_left(cd, -i, 0, length)
    result += res
print(result)

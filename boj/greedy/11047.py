N, K = list(map(int, input().split()))
A = []
count = 0
for i in range(0, N):
    A.append(int(input()))
A.reverse()
for i in A:
    if(i <= K):
        count += (K // i)
        K = K - (i * (K // i))
print(count)
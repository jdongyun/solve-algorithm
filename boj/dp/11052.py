n = int(input())
p = [0] + list(map(int, input().split()))
d = [0] * (n+1)
for i in range(1, n+1):
    max_value = p[i]
    for j in range(1, i+1):
        if i % j == 0:
            max_value = max(max_value, p[j] * (i // j)) # 한 가지 카드팩 여러 번 선택
        max_value = max(max_value, d[i-j] + d[j]) #i-j, j번째 카드팩 선택
    d[i] = max_value
print(d[n])

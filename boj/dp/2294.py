n, k = map(int, input().split())
coin = set() 
for _ in range(n):
    coin.add(int(input()))
coin = sorted(list(coin))
d = [int(1e9)] * 100001
for i in coin:
    d[i] = 1
for i in range(coin[0] + 1, k + 1):
    for j in coin:
        if i - j < 0: break
        d[i] = min(d[i], d[j] + d[i - j])
print(d[k] if d[k] != int(1e9) else -1)

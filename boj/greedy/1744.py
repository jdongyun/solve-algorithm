n = int(input())
g = [int(input()) for i in range(n)]
g.sort()

neg = 0
pos = n-1
ret = 0

while neg < n - 1:
    if g[neg] > 0 or g[neg + 1] > 0:
        break
    ret += max(g[neg] * g[neg + 1], g[neg] + g[neg + 1])
    neg += 2

while pos > 0:
    if g[pos] < 0 or g[pos - 1] < 0:
        break
    ret += max(g[pos] * g[pos - 1], g[pos] + g[pos - 1])
    pos -= 2
   
for i in range(neg, pos + 1):
    ret += g[i]

print(ret)

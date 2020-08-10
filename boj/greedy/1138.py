n = int(input())
l = list(map(int, input().split()))
ret = [0] * n
for i in range(n):
  data = l[i]
  for j in range(n):
    if ret[j] == 0:
      if data == 0:
        ret[j] = i + 1
        break
      data -= 1
print(' '.join(map(str, ret)))
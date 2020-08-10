
n, k = map(int, input().split())
prods = list(map(lambda x: int(x) - 1, input().split()))
now_used = set()
count = 0
for i in range(k):
  if prods[i] in now_used:
    continue
  elif len(now_used) < n:  # 자리 꽉 안참
    now_used.add(prods[i])
  else:
    later_used = [k+1] * k  #기본값을 k+1로 지정하여 아예 뒤에 사용하지 않을 때를 최대로 지정
    for j in range(k-1, i, -1):
      later_used[prods[j]] = j
    max_later = list(now_used)[0]
    for j in now_used:
      if later_used[max_later] < later_used[j]:
        max_later = j
    now_used.remove(max_later)
    now_used.add(prods[i])
    count += 1
print(count)
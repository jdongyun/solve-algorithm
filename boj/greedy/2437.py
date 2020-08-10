n = int(input())
weights = list(map(int, input().split()))
weights.sort()
sum_weight = 0
for weight in weights:
  if sum_weight + 1 < weight:
    break
  sum_weight += weight
print(sum_weight + 1)
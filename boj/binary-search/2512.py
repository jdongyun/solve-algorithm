n = int(input())
budgets = list(map(int, input().split()))
m = int(input())
start = 0
end = max(budgets)
result = 0
while start <= end:
    mid = (start + end) // 2
    sum_budgets = 0
    for b in budgets:
        sum_budgets += min(b, mid)
    if sum_budgets <= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)

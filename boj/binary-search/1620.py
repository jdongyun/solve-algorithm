n, m = map(int, input().split())
names = [input() for _ in range(n)]
order_by_idx = [(i+1, e) for i, e in enumerate(names)]
order_by_name = sorted(order_by_idx, key=lambda x:x[1])
questions = [input() for _ in range(m)]

def find(arr, target):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid][1] == target:
            return arr[mid][0]
        elif arr[mid][1] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for q in questions:
    if q.isdigit():
        print(order_by_idx[int(q) - 1][1])
    else:
        print(find(order_by_name, q))

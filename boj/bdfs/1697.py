from collections import deque
n, k = map(int, input().split())
if (n-k) >= 0:
    print(n-k)
    exit(0)
visited = [False] * 100_001
queue = deque([(n, 0)])
while queue:
    i, t = queue.popleft()
    if i == k:
        print(t)
        break
    for new_i in [i-1, i+1, 2*i]:
        if 0 <= new_i <= 100_000 and not visited[new_i]:
            visited[new_i] = True
            queue.append((new_i, t+1))

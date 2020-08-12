from collections import deque
n, m, k, x = map(int, input().split())
roads = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    roads[a].append(b)
dist = [-1] * (n+1)
queue = deque([x])
dist[x] = 0

while queue:
    q = queue.popleft()
    for road in roads[q]:
        if dist[road] == -1:
            queue.append(road)
            dist[road] = dist[q] + 1
            
check = False
for i in range(n+1):
    if dist[i] == k:
        check = True
        print(i)
if not check:
    print(-1)
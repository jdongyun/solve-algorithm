from collections import deque
n, m = map(int, input().split())
bridges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    bridges[a].append((b, c))
    bridges[b].append((a, c))
x, y = map(int, input().split())

def bfs(visited, start, end, over):
    queue = deque([start])
    visited[start] = True
    while queue:
        i = queue.popleft()
        if end == i:
            return True
        for b in range(len(bridges[i])):
            _b, _c = bridges[i][b]
            if not visited[_b]: 
                if _c >= over:
                    queue.append(_b)
                    visited[_b] = True
    return False

start = 1
end = 1_000_000_000
result = 0
while start <= end:
    mid = (start + end) // 2
    if bfs([False] * (n+1), x, y, mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)

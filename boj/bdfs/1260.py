from collections import deque
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
for i in graph:
    i.sort()

def dfs(graph, i, visited):
    visited[i] = True 
    print(i, end=' ')
    for next_node in graph[i]:
        if not visited[next_node]:
            dfs(graph, next_node, visited)

def bfs(graph, i):
    visited = [False] * (n + 1)
    queue = deque([i])
    while queue:
        q = queue.popleft()
        if visited[q]:
            continue
        visited[q] = True
        print(q, end=' ')
        for next_node in graph[q]:
            if not visited[next_node]:
                queue.append(next_node)

visited = [False] * (n+1)
dfs(graph, v, visited)
print()

bfs(graph, v)
print()

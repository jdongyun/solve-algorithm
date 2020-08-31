import sys
input = lambda: sys.stdin.readline().rstrip() 
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

def dfs(graph, i, visited, count):
    if count == 5: 
        print("1")
        exit(0)
    visited[i] = True
    for next_node in graph[i]:
        if not visited[next_node]:
            dfs(graph, next_node, visited, count + 1)
    visited[i] = False

for i in range(n):
    dfs(graph, i, [False] * n, 1)
print(0)

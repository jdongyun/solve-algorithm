import sys
import collections
import heapq
sys.setrecursionlimit(int(1e5))
input = lambda: sys.stdin.readline().rstrip()


def dijkstra(graph, start):
    n = len(graph)
    distance = [int(1e9)] * n
    q = [(0, start)]
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for j, d in graph[now]:
            cost = dist + d
            if cost < distance[j]:
                distance[j] = cost
                heapq.heappush(q, (cost, j))
    return distance


n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j, d = map(int, input().split())
    graph[i].append((j, d))

results = [int(1e9)] * (n+1)
for i in range(1, n+1):
    res = dijkstra(graph, i)
    results[i] = res[x]

res = dijkstra(graph, x)
for i in range(1, n+1):
    results[i] += res[i]
print(max(results[1:]))


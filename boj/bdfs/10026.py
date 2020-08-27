import sys
from collections import deque

input = sys.stdin.readline

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(graph, n):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            queue = deque([(i, j)])
            visited[i][j] = True
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if not visited[nx][ny] and graph[nx][ny] == graph[i][j]:
                            queue.append((nx, ny))
                            visited[nx][ny] = True
            count += 1
    return count

n = int(input())
graph = [list(input()) for _ in range(n)]
print(bfs(graph, n), end=' ')
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R': # 적록색약은 빨간색과 녹색을 동일하게 인식하므로
            graph[i][j] = 'G'
print(bfs(graph, n))

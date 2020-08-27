import sys
from collections import deque

input = sys.stdin.readline

directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)] # 대각선도 포함

def bfs(graph, w, h):
    visited = [[False] * w for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] or graph[i][j] == 0:
                continue
            queue = deque([(i, j)])
            visited[i][j] = True
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < h and 0 <= ny < w:
                        if not visited[nx][ny] and graph[nx][ny] == 1:
                            queue.append((nx, ny))
                            visited[nx][ny] = True
            count += 1
    return count

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    print(bfs(graph, w, h))

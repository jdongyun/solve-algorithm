from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

queues = [deque() for _ in range(k+1)]
for i in range(n):
    for j in range(n):
        if graph[i][j] > 0:
            queues[graph[i][j]].append((i, j))

directions = [(-1,0), (0,1),(1,0), (0,-1)]
for second in range(s):
    for i, queue in enumerate(queues):
        if not queue:
            continue
        for _ in range(len(queue)): # 처음에 큐에 담겨 있던 모든 위치를 방문해야 한다
            tx, ty = queue.popleft()
            for direction in directions:
                nx, ny = tx + direction[0], ty + direction[1]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    graph[nx][ny] = i
print(graph[x-1][y-1])

        

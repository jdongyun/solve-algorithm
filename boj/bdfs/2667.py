from collections import deque
n = int(input())
maps = [list(map(int, input())) for _ in range(n)]
visited = [[False] * (n) for _ in range(n)]
directions = [(-1,0), (1, 0), (0, 1), (0, -1)]

queue = deque()
apt_counts = []
for i in range(n):
    for j in range(n):
        count = 0
        queue.append((i, j))
        while queue:
            x, y = queue.popleft()
            if maps[x][y] == 0 or visited[x][y]:
                continue
            visited[x][y] = True
            count += 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if maps[nx][ny] == 1 and not visited[nx][ny]:
                        queue.append((nx, ny))
        if count > 0:
            apt_counts.append(count)

print(len(apt_counts))
apt_counts.sort()
print('\n'.join(map(str, apt_counts)))

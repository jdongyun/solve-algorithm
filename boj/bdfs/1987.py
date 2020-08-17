#해결은 했지만 시간이 매우 오래 걸렸다. BFS로 해결하면 더 빠를 것 같다.
r, c = map(int, input().split())
data = [list(input()) for _ in range(r)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visited = [False] * (ord('Z') - ord('A') + 1)
length = 0
def dfs(x, y, count):
    global length
    length = max(length, count)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            vi = ord(data[nx][ny]) - ord('A')
            if visited[vi]:
                continue
            visited[vi] = True
            dfs(nx, ny, count + 1)
            visited[vi] = False

visited[ord(data[0][0]) - ord('A')] = True
dfs( 0, 0, 1)
print(length)

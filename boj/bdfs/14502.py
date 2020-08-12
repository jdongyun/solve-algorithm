from itertools import combinations
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
temp = [[0] * m for _ in range(n)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
result = 0
viruses = []
spaces = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            spaces.append((i, j))
        elif data[i][j] == 2:
            viruses.append((i, j))

def get_score():
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1
    return count

def virus(x, y):
    for direction in directions:
        nx, ny = x + direction[0], y + direction[1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if temp[nx][ny] == 0:
            temp[nx][ny] = 2
            virus(nx, ny)

result = 0
for combination in list(combinations(spaces, 3)):
    for i in range(n):
        for j in range(m):
            temp[i][j] = data[i][j]
    for x,y in combination:
        temp[x][y] = 1
    for x,y in viruses:
        virus(x, y)
    result = max(result, get_score())
print(result)


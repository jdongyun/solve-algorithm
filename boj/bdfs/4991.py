import sys
from collections import deque
from itertools import combinations, permutations
input = lambda: sys.stdin.readline().rstrip() 
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    board = [list(input()) for _ in range(h)]

    trash = [] # 더러운 칸 x,y 배열
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'o':
                trash.append((0, i, j))
                board[i][j] = '.'
    c = 1
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                trash.append((c, i, j))
                c += 1

    #(x1,y1) (x2,y2) 사이의 최단거리 계산
    def find_min(x1, y1, x2, y2):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * w for _ in range(h)]
        visited[x1][y1] = True
        q = deque([(x1, y1, 0)])
        while q:
            x, y, d = q.popleft()
            if x == x2 and y == y2:
                return d
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w:
                    if (board[nx][ny] == '.' or board[nx][ny] == '*') and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny, d + 1))
        return int(1e9)

    # trash[i], trash[j] 사이의 최단거리 계산
    dist = [[int(1e9)] * len(trash) for _ in range(len(trash))]
    for c in trash[1:]: # 0부터 trash[i]까지의 거리 계산
        i2, x2, y2 = c
        dist[0][i2] = dist[i2][0] = find_min(trash[0][1], trash[0][2], x2, y2)

    for c1, c2 in combinations(trash[1:], 2):
        i1, x1, y1 = c1
        i2, x2, y2 = c2
        dist[i1][i2] = dist[i2][i1] = find_min(x1, y1, x2, y2)

    min_dist = int(1e9)
    for perm in permutations(list(range(1, len(trash))), len(trash) -1):
        i = perm[0]
        min_tmp = dist[0][i] #0에서 i까지 미리 계산
        for p in perm[1:]: #쓰레기들 사이의 거리 게산
            ni = p
            min_tmp += dist[i][ni]
            i = ni
        min_dist = min(min_dist, min_tmp)
    print(min_dist if min_dist != int(1e9) else -1)

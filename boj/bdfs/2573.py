import sys
import collections
import copy
import heapq
sys.setrecursionlimit(int(1e5))
input = lambda: sys.stdin.readline().rstrip() 

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for year in range(10_000_000):
    new_board = copy.deepcopy(board)
    visited = [[0] * m for _ in range(n)]
    count = 0
    # 빙산 개수 찾기.
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0 or visited[i][j] > 0:
                continue
            count += 1
            visited[i][j] = count
            q = collections.deque([(i, j)])
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if board[nx][ny] > 0 and visited[nx][ny] == 0:
                            visited[nx][ny] = count
                            q.append((nx, ny))
    
    if count == 0:
        print(0)
        break
    if count > 1:
        # 둘 이상으로 쪼개짐.
        print(year)
        break

    # 빙산 녹이기.
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                cnt = 0
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if board[nx][ny] == 0:
                            cnt += 1
                new_board[i][j] = max(board[i][j] - cnt, 0)

    board = new_board
    

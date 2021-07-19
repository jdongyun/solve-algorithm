import sys
import collections
import heapq
sys.setrecursionlimit(int(1e5))
input = lambda: sys.stdin.readline().rstrip() 

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(x, y):
    global dp
    if dp[x][y] > -1:
        return dp[x][y]
    result = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if board[x][y] < board[nx][ny]:
                result = max(result, dfs(nx, ny) + 1)
    dp[x][y] = result
    return result

res = 0
for i in range(n):
    for j in range(n):
        res = max(res, dfs(i, j))
print(res + 1)

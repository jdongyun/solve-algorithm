from collections import deque
from copy import deepcopy
import heapq
from itertools import combinations, permutations
from itertools import combinations_with_replacement
import sys

input = lambda: sys.stdin.readline().rstrip() 
test = True
if test:
    try:
        sys.stdin = open('input_data.txt', 'r')
        print('sys.stdin = input.txt')
    except FileNotFoundError:
        pass

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
virus_board = [[0] * n for _ in range(n)]
viruses = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            virus_board[i][j] = 1
            continue
        elif board[i][j] == 2:
            viruses.append((i, j))
            virus_board[i][j] = 2

def run(virus_comb):
    new_board = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    q = deque()
    for x, y in virus_comb:
        q.append((x, y, 0))
        visited[x][y] = True
    
    while q:
        x, y, t = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and virus_board[nx][ny] != 1:
                    visited[nx][ny] = True
                    new_board[nx][ny] = t + 1
                    q.append((nx, ny, t + 1))
    temp_result = 0
    for i in range(n):
        for j in range(n):
            if new_board[i][j] == 0 and not visited[i][j] and virus_board[i][j] == 0:
                return int(1e9)
            if visited[i][j] and virus_board[i][j] == 0:
                temp_result = max(temp_result, new_board[i][j])
    return temp_result

result = int(1e9)
for virus_comb in combinations(viruses, m):
    result = min(result, run(virus_comb))
print(-1 if result == int(1e9) else result)
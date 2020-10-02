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


directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
n, m, k = map(int, input().split())
annual_food = [list(map(int, input().split())) for _ in range(n)]
infos = [[deque() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    x, y = x - 1, y - 1
    infos[x][y].append(z)

now_food = [[5] * n for _ in range(n)]
for _ in range(k):
    for i in range(n):
        for j in range(n):
            for z in range(len(infos[i][j])):
                if infos[i][j][z] <= now_food[i][j]:
                    now_food[i][j] -= infos[i][j][z]
                    infos[i][j][z] += 1
                else:
                    while z < len(infos[i][j]):
                        now_food[i][j] += infos[i][j].pop() // 2
                    break


    for i in range(n):
        for j in range(n):
            for k in range(len(infos[i][j])):
                if infos[i][j][k] % 5 == 0:
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            infos[nx][ny].appendleft(1)
    
    for i in range(n):
        for j in range(n):
            now_food[i][j] += annual_food[i][j]

cnt = 0
for i in range(n):
    for j in range(n):
        cnt += len(infos[i][j])

print(cnt)
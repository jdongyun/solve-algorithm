from collections import deque
from copy import deepcopy
import decimal
import heapq
from itertools import combinations, permutations
from itertools import combinations_with_replacement
import sys

sys.setrecursionlimit(100_000)
input = lambda: sys.stdin.readline().rstrip() 
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

test = True
if test:
    try:
        sys.stdin = open('input_data.txt', 'r')
        print('sys.stdin = input.txt')
    except FileNotFoundError:
        pass

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
shark_loc = []
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            shark_loc.append((board[i][j], i, j))
            board[i][j] = 0

shark_smell_id = [[0] * n for _ in range(n)]
shark_smell_time = [[0] * n for _ in range(n)]
shark_direction = [0] + [x-1 for x in list(map(int, input().split()))]
priority = [[] for _ in range(m + 1)]
for i in range(1, m+1):
    for _ in range(4):
        p = [x-1 for x in list(map(int, input().split()))]
        priority[i].append(p)

def set_smell(shark_loc):
    global shark_smell_id, shark_smell_time
    for idx, x, y in shark_loc:
        shark_smell_id[x][y] = idx
        shark_smell_time[x][y] = k

def move_sharks(shark_loc):
    global shark_smell_id, shark_smell_time, shark_direction
    tmp_check = [[int(1e9)] * n for _ in range(n)]
    for idx, x, y in shark_loc:

        #아무 냄새 없는 칸 찾기
        find = False
        for d in priority[idx][shark_direction[idx]]:
            nx, ny = x + delta[d][0], y + delta[d][1]
            if 0 <= nx < n and 0 <= ny < n:
                if shark_smell_id[nx][ny] == 0:
                    find = True
                    if tmp_check[nx][ny] < idx:
                        break
                    
                    tmp_check[nx][ny] = idx
                    shark_direction[idx] = d
                    break
                    
        
        #아무 냄새 없는 칸을 못찾으면 내 냄새 칸 찾기
        if not find:
            for d in priority[idx][shark_direction[idx]]:
                nx, ny = x + delta[d][0], y + delta[d][1]
                if 0 <= nx < n and 0 <= ny < n:
                    if shark_smell_id[nx][ny] == idx:
                        tmp_check[nx][ny] = idx
                        shark_direction[idx] = d
                        break
    
    ret = []
    for i in range(n):
        for j in range(n):
            if tmp_check[i][j] != int(1e9):
                ret.append((tmp_check[i][j], i, j))
    return ret

def remove_smell():
    global shark_smell_time, shark_smell_id
    for i in range(n):
        for j in range(n):
            if shark_smell_id[i][j] > 0:
                shark_smell_time[i][j] -= 1
                if shark_smell_time[i][j] == 0:
                    shark_smell_id[i][j] = 0

    
def check_only_one(shark_loc):
    if len(shark_loc) == 1 and shark_loc[0][0] == 1:
        return True
    return False
    
for t in range(1001):
    #1번만 남아있음 체크
    if check_only_one(shark_loc):
        print(t)
        exit(0)
    
    #처음엔 자신의 위치에 냄새를 뿌린다
    set_smell(shark_loc)

    #상어가 움직인다
    new_shark_loc = move_sharks(shark_loc)
    shark_loc = new_shark_loc

    #상어 냄새 빼준다
    remove_smell()

print(-1)


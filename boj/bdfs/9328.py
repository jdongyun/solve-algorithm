import sys
from collections import deque
from itertools import combinations, permutations
input = lambda: sys.stdin.readline().rstrip() 

def is_door(door):
    return ord('A') <= ord(door) <= ord('Z')
def is_key(key):
    return ord('a') <= ord(key) <= ord('z')
def door_to_key(door):
    return chr(ord(door) + 32)
def key_to_door(key):
    return chr(ord(key) - 32)
def have_key(key, keys):
    return key in keys
def have_key_for_door(door, keys):
    return have_key(door_to_key(door), keys)


for _ in range(int(input())):
    h, w = map(int, input().split())
    bb = [list(input()) for _ in range(h)]
    board = [['.'] * (w + 2) for _ in range(h+2)]
    for i in range(1, h+1):
        for j in range(1, w+1):
            board[i][j] = bb[i-1][j-1]
    keys = input()
    if keys == '0': keys = ''
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    q = deque([(0, 0)])
    visited = [[False] * (w+2) for _ in range(h+2)]
    
    cnt = 0
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h + 2 and 0 <= ny < w + 2:
                if board[nx][ny] == '.' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                if is_door(board[nx][ny]) and have_key_for_door(board[nx][ny], keys): 
                    board[nx][ny] = '.'
                    q.append((nx, ny))
                if is_key(board[nx][ny]):
                    if not have_key(board[nx][ny], keys): # 키가 없으면 키 추가
                        keys += board[nx][ny]
                        visited = [[False] * (w+2) for _ in range(h+2)] # 처음부터 다시 탐색
                    visited[nx][ny] = True
                    board[nx][ny] = '.'
                    q.append((nx, ny))
                if board[nx][ny] == '$' and not visited[nx][ny]: # 문서를 찾으면 문서 개수 더하고 중복탐색 방지 위해 문서 삭제
                    cnt += 1
                    board[nx][ny] = '.'
                    visited[nx][ny] = True
                    q.append((nx, ny))
    print(cnt)

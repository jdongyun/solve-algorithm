import sys

def new_direction(direction, time):
  if time == 'L':
    direction -= 1
    if direction == -1:
      direction = 3
  elif time == 'D':
    direction += 1
    if direction == 4:
      direction = 0
  return direction

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
board = [[0] * n for _ in range(n)]
for _ in range(k):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  board[x-1][y-1] = 1
l = int(sys.stdin.readline())
times = []
for _ in range(l):
  x, c = sys.stdin.readline().rstrip().split()
  x = int(x)
  times.append((x, c))



directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북동남서
direction = 1
x, y = 0, 0
history = [(0, 0)]
board[0][0] = 2
length = 1
for t in range(1, 10000):
  ny, nx = y + directions[direction][0], x + directions[direction][1]
  if nx < 0 or nx >= n or ny < 0 or ny >= n:
    print(t)
    break
  if board[ny][nx] == 2:
    print(t)
    break
  x, y = nx, ny
  history.append((y, x))
  if board[y][x] == 0:
    d = history.pop(0)
    board[d[0]][d[1]] = 0 
    board[y][x] = 2 # 뱀의 위치
  elif board[y][x] == 1:
    length += 1
    board[y][x] = 2 # 뱀의 위치
  if len(times) > 0 and times[0][0] == t:
    direction = new_direction(direction, times[0][1])
    times.pop(0)
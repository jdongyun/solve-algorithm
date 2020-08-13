from itertools import combinations
n = int(input())
d = [list(input().split()) for _ in range(n)]
teachers = []
spaces = []

for i in range(n):
    for j in range(n):
        if d[i][j] == 'X':
            spaces.append((i, j))
        elif d[i][j] == 'T':
            teachers.append((i, j))

def check(data):
    for teacher in teachers:
        ti, tj = teacher
        for i in range(ti, -1, -1):
            if data[i][tj] == 'S':
                return False
            elif data[i][tj] == 'O':
                break
        for i in range(ti, n):
            if data[i][tj] == 'S':
                return False
            elif data[i][tj] == 'O':
                break
        for j in range(tj, -1, -1):
            if data[ti][j] == 'S':
                return False
            elif data[ti][j] == 'O':
                break
        for j in range(tj, n):
            if data[ti][j] == 'S':
                return False
            elif data[ti][j] == 'O':
                break
    return True

for combination in list(combinations(spaces, 3)):
    temp = [r[:] for r in d]
    for comb in combination:
        i, j = comb
        temp[i][j] = 'O'
    if check(temp):
        print("YES")
        exit(0)
print("NO")

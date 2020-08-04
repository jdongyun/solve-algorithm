import sys
for _ in range(0, int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    grades = []
    for i in range(0, n):
        a, b = map(int, sys.stdin.readline().split())
        grades.append((i, a, b))
    grades = sorted(grades, key=lambda x: x[1])
    cutline = grades[0][2]
    ret = 1
    for i in range(1, n):
        if grades[i][2] < cutline:
            ret += 1
            cutline = grades[i][2]
    print(ret)
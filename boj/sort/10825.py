import sys
n = int(sys.stdin.readline().rstrip())
students = []
for i in range(n):
    students.append(sys.stdin.readline().rstrip().split())
    for j in range(1, 4):
        students[i][j] = int(students[i][j])

students = sorted(students, key=lambda x: x[0])
students = sorted(students, key=lambda x: x[3], reverse=True)
students = sorted(students, key=lambda x: x[2])
students = sorted(students, key=lambda x: x[1], reverse=True)
for student in students:
    print(student[0])

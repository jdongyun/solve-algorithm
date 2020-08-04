import sys
n, m = map(int, sys.stdin.readline().split())
pkg = []
one = []
for _ in range(0, m):
    x, y = map(int, sys.stdin.readline().split())
    if x > 6 * y:
        pkg.append(6*y)
    else:
        pkg.append(x)
    one.append(y)
pkg.sort()
one.sort()
ret = (n // 6) * pkg[0]
if pkg[0] > one[0] * (n % 6):
    ret += one[0] * (n % 6)
else:
    ret += pkg[0]
print(ret)
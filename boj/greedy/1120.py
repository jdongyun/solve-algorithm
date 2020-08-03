import sys
a, b = sys.stdin.readline().split()
min_diff = 100_000_000  # max
for i in range(0, len(b) - len(a) + 1):
    diff = 0
    for j in range(i, len(a)+i):
        if a[j-i] != b[j]:
            diff += 1
    if diff < min_diff:
        min_diff = diff
print(min_diff)

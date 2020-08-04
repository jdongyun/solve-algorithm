import sys
k = int(sys.stdin.readline())
ineq = sys.stdin.readline().split()
ineq.append('')
max_num = []
max_val = 9
max_cnt = 0

for i in range(0, k+1):
    if ineq[i] == '<':
        max_cnt += 1
    else:
        start_val = max_val - max_cnt
        for j in range(0, max_cnt + 1):
            max_num.append(start_val)
            start_val += 1
        max_val = max_val - max_cnt - 1
        max_cnt = 0
print(''.join(map(str, max_num)))

min_num = []
min_val = 0
min_cnt = 0
for i in range(0, k+1):
    if ineq[i] == '>':
        min_cnt += 1
    else:
        start_val = min_val + min_cnt
        for j in range(0, min_cnt + 1):
            min_num.append(start_val)
            start_val -= 1
        min_val = min_val + min_cnt + 1
        min_cnt = 0
print(''.join(map(str, min_num)))
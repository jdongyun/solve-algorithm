import sys
from functools import reduce
N = list(str(sys.stdin.readline()))[:-1]
N = sorted(N, reverse=True)
sum_digit = reduce(lambda acc, cur: acc+cur, list(map(int, N)), 0)
if sum_digit % 3 == 0 and N[-1] == '0':
    print(''.join(N))
else:
    print('-1')
import sys
from functools import reduce
exp = list(map(str, sys.stdin.readline().split('-')))
for i, e in enumerate(exp):
    exp[i] = reduce(lambda acc, cur: acc + cur, list(map(int, e.split('+'))), 0)
print(reduce(lambda acc, cur: acc - cur, exp, 2*exp[0]))
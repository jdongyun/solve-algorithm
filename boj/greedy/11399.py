from functools import reduce
N = int(input())
P = list(map(int, input().split()))
P.sort()
ret = [a*b for a,b in zip(P, list(range(N, 0, -1)))]
print(reduce(lambda acc, cur: acc+cur, ret, 0))

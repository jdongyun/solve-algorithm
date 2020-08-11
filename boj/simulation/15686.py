import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().rstrip().split())
infos = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
restaurants = []
houses = []
for i in range(n):
    for j in range(n):
        if infos[i][j] == 1:
            houses.append((i, j))
        elif infos[i][j] == 2:
            restaurants.append((i, j))
min_count = 999_999_999
for rest_comb in combinations(restaurants, m):
    count = 0
    for h in houses:
        i, j = h
        min_dist = 999_999_999
        for r in rest_comb:
            ri, rj = r
            min_dist = min(min_dist, abs(i-ri) + abs(j-rj))
        count += min_dist
    min_count = min(count, min_count)
print(min_count)
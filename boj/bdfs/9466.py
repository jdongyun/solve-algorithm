import sys
import collections
import heapq
sys.setrecursionlimit(int(1e5))
input = lambda: sys.stdin.readline().rstrip() 

def solve(start):
    global nums, visited, finished
    stack = [start]
    next = nums[start]

    visited[start] = True
    while not visited[next] and finished[next] == -1:
        visited[next] = True
        stack.append(next)
        next = nums[next]

    result = 1 if finished[next] == -1 else 0
    while stack:
        i = stack.pop()
        visited[i] = False
        finished[i] = result
        if i == next:
            result = 0

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(lambda x: int(x) - 1, input().split()))
    if n == 1 and nums[0] == 0:
        print(1)
        continue

    finished = [-1] * n
    visited = [False] * n
    
    for i in range(n):
        if finished[i] > -1:
            continue
        solve(i)

    print(n - sum(finished))

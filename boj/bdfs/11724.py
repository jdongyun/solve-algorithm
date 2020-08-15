n, m = map(int, input().split())
graphs = [[] for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    graphs[i].append(j)
    graphs[j].append(i)
count = 0
visited = [False] * (n+1)
for i in range(1, n+1):
    stack = [i]
    flag = False
    while len(stack) > 0:
        s = stack.pop()
        if visited[s]:
            continue
        visited[s] = True
        flag = True
        for j in graphs[s]:
            if not visited[j]:
                stack.append(j)
    if flag:
        count += 1
print(count)

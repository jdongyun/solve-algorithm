import heapq
n, k = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(n)] # m v
bags = [int(input()) for _ in range(k)]
infos.sort()
bags.sort()

heap = []
info_i = 0
sum_value = 0
for bag in bags:
    while info_i < n and infos[info_i][0] <= bag:
        heapq.heappush(heap, -infos[info_i][1]) 
        info_i += 1
    if len(heap) > 0:
        sum_value += -heapq.heappop(heap)
print(sum_value)

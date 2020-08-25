import sys
input = sys.stdin.readline
n = int(input())
dist = list(map(int, input().split()))
dist.append(0) # 제일 오른쪽인 노드는 도착점이므로 거리가 0

price = list(map(int, input().split()))
new_price = []
length = sum(dist)
for i in range(n):
    new_price.append((price[i], length, i))
    length -= dist[i] # 도착점까지의 거리
new_price.sort() # 기름값 낮은 순으로 정렬

length = sum(dist)
cost = 0
pointer = 0 #이미 계산 완료한 곳까지의 거리를 저장
for p, l, i in new_price:
    if pointer < l and pointer < length: # 계산하지 않은 구간일 때
        cost += (l - pointer) * p # 노드의 위치에서 계산한 구간을 뺀 거리에 대해서 계산
        pointer = l
print(cost)

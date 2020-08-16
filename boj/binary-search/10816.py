import bisect

n = int(input())
n_card = list(map(int, input().split()))
m = int(input())
m_card = list(map(int, input().split()))
n_card.sort()

for c in m_card:
    print(bisect.bisect_right(n_card, c, 0, n) - bisect.bisect_left(n_card, c, 0, n), end=' ')

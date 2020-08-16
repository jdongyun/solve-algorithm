# Set으로 해결
n = int(input())
n_card = list(map(int, input().split()))
m = int(input())
m_card = list(map(int, input().split()))
s = set(n_card)
for c in m_card:
    if c in s:
        print('1', end=' ')
    else:
        print('0', end=' ')

# 이진 탐색으로 해결
n = int(input())
n_card = list(map(int, input().split()))
m = int(input())
m_card = list(map(int, input().split()))
n_card.sort()

def find(target):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if n_card[mid] == target:
            return True
        elif n_card[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False
for i in m_card:
    if find(i):
        print('1', end=' ')
    else:
        print('0', end=' ')

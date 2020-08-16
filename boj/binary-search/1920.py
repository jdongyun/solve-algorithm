# Set을 사용한 방법
n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))
s = set(n_arr)
for a in m_arr:
    if a in s:
        print(1)
    else:
        print(0)


#이진 탐색을 이용한 방법
n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))
n_arr.sort()

def find(target):
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        if n_arr[mid] == target:
            return True
        elif n_arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

for i in m_arr:
    if find(i):
        print(1)
    else:
        print(0)
    

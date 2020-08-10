n, l = map(int, input().split())
locations = list(map(int, input().split()))
locations.sort()
tape_count = 0
tape_end = -1
for i in range(n):
  if tape_end < locations[i]:
    tape_count += 1
    tape_end = locations[i] + l - 1  # 이 좌표까지 막을 수 있다
print(tape_count)
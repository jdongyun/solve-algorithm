import sys
N = int(sys.stdin.readline())
meeting = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    meeting.append((start, end))
meeting = sorted(meeting, key=lambda t: t[0])
meeting = sorted(meeting, key=lambda t: t[1])

ret = 0
start_time = 0
for time in meeting:
    if time[0] >= start_time:
        start_time = time[1]
        ret += 1
print(ret)
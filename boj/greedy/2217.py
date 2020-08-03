import sys
N = int(sys.stdin.readline())
max_weights = []
for _ in range(0, N):
    max_weights.append(int(sys.stdin.readline()))
max_weights = sorted(max_weights, reverse=True)
ret = max_weights[0]
for i, weight in enumerate(max_weights):
    if ret <= (weight * (i + 1)):
        ret = (weight * (i + 1))
print(ret)
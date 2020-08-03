import sys
N = int(sys.stdin.readline())
changes = 1000 - N
coins = [500, 100, 50, 10, 5, 1]

count = 0
for coin in coins:
    if changes >= coin:
        count += changes // coin
        changes = changes % coin
print(count)
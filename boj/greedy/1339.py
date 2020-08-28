n = int(input())
vocas = [input() for _ in range(n)]
counts = [0] * 26
for voca in vocas:
    rev = reversed(voca)
    weight = 1
    for v in rev:
        counts[ord(v) - ord('A')] += weight
        weight *= 10
zipped = list(zip(map(chr, range(ord('A'), ord('A') + 26)), counts))
zipped.sort(key=lambda x: x[1], reverse=True)

count = 0
mul = 9
for _, weight in zipped:
    count += weight * mul
    mul -= 1

print(count)

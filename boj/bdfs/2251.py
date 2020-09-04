import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
vol = [[[False for _ in range(201)] for _ in range(201)] for _ in range(201)]
a, b, c = map(int, input().split())
s = set()
q = deque([(0, 0, c)])

def atob(nowa, nowb, fullb):
    if nowa + nowb > fullb:
        return nowa - (fullb - nowb), fullb
    else:
        return 0, nowa + nowb

def btoa(nowb, nowa, fulla):
    r = atob(nowb, nowa, fulla)
    return r[1], r[0]

while q:
    ta, tb, tc = q.popleft()
    fr = [(*atob(ta, tb, b), tc), (*btoa(tb, ta, a), tc), 
            (ta, *atob(tb, tc, c)), (ta, *btoa(tc, tb, b)),
            (atob(ta, tc, c)[0], tb, atob(ta, tc, c)[1]),
            (btoa(tc, ta, a)[0], tb, btoa(tc, ta, a)[1])]
    for na, nb, nc in fr:
        if 0 <= na <= a and 0 <= nb <= b and 0 <= nc <= c and na + nb + nc == c:
            if not vol[na][nb][nc]:
                vol[na][nb][nc] = True
                if na == 0:
                    s.add(nc)
                q.append((na, nb, nc))
print(*sorted(list(s)))

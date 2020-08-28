case_count = 1
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    ret = l * (v // p)
    ret += min(v % p, l) 
    print(f'Case {case_count}: {ret}')
    case_count += 1

n, m = map(int, input().split())

_min = 10**13

for a in range(int(-(-(m**0.5) // 1))):
    b = -(-m // (a + 1))
    if b <= n and (a + 1) <= n:
        _min = min(_min, (a + 1) * b)

if _min == 10**13:
    _min = -1

print(_min)

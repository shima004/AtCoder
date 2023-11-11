n = int(input())
w, x = [], []
ans = [0 for i in range(24)]
for _ in range(n):
    _w, _x = map(int, input().split())
    w.append(_w)
    x.append(_x)
    ans[_x] += _w

width = 9
_max = 0
for i in range(24):
    if i + width > 24:
        a = sum(ans[i:24]) + sum(ans[0 : i + width - 24])
    else:
        a = sum(ans[i : i + width])
    if a > _max:
        _max = a

print(_max)

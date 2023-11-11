n = int(input())
items = []
for _ in range(n):
    _t, _d = map(int, input().split())
    items.append((_t, _d, _t + _d))

items.sort(key=lambda x: (x[2], x[0]), reverse=True)

ans = 0
now = 1
while items:
    t, d, _ = items.pop()
    if now <= (t + d):
        ans += 1
        if now < t:
            now = t + 1
        else:
            now += 1

print(ans)

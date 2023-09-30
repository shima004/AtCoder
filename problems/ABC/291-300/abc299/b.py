n, t = map(int, input().split())

c = list(map(int, input().split()))
r = list(map(int, input().split()))

if t not in c:
    t = c[0]

ans = 0
_max = 0
for i in range(n):
    if c[i] == t:
        if r[i] > _max:
            _max = r[i]
            ans = i+1
print(ans)

n, m = map(int, input().split())
c = input().split()
d = input().split()
p = list(map(int, input().split()))

pl = {}
for i in range(m):
    pl[d[i]] = p[i + 1]

ans = 0
for i in c:
    if i in pl:
        ans += pl[i]
    else:
        ans += p[0]

print(ans)

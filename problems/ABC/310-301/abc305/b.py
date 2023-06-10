p, q = input().split()
d = [3, 1, 4, 1, 5, 9]
point = ["A", "B", "C", "D", "E", "F", "G"]

s = point.index(p) if point.index(p) < point.index(q) else point.index(q)
e = point.index(p) if point.index(p) > point.index(q) else point.index(q)

ans = 0
for i in range(s, e):
    ans += d[i]

print(ans)

from itertools import product

n = int(input())
r = list(input())
c = list(input())
# check include a, b, c
if r.count("A") == 0 or r.count("B") == 0 or r.count("C") == 0:
    print(0)
    exit()
# check include a, b, c
if c.count("A") == 0 or c.count("B") == 0 or c.count("C") == 0:
    print(0)
    exit()

r_p = []
c_p = []
for i in product([0, 1], repeat=n):
    # 1が3つあるか
    if i.count(1) == 3:
        a = set()
        b = set()
        for j in range(n):
            if i[j] == 1:
                a.add(r[j])
                b.add(c[j])
        if len(a) == 3:
            r_p.append(i)
        if len(b) == 3:
            c_p.append(i)

for i in r_p:
    f = [list("." * n) for _ in range(n)]
    for j in range(n):
        if i[j] == 1:
            f[j][0] = r[j]
    for j in c_p:
        for k in range(n):
            if j[k] == 1:
                f[0][k] = c[k]
            else:
                f[0][k] = "."
        for k in range(n):
            print(f[k])

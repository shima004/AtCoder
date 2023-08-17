n = int(input())
a, b = [], []
for i in range(n):
    _a, _b = map(int, input().split())
    a.append(_a)
    b.append(_b)

from fractions import Fraction

pl = []
for i in range(n):
    f = Fraction(a[i], b[i] + a[i])
    pl.append([f.numerator / f.denominator, -i])

pl.sort(reverse=True, key=lambda x: (x[0], x[1]))

for i in range(n):
    print(-pl[i][1] + 1, end=" ")
print()

s = list(map(int, input().split()))

m = -1
f = False
for i in s:
    if m > i:
        f = True
        break
    m = i

for i in s:
    if i > 675 or i < 100:
        f = True
        break

for i in s:
    if i % 25 != 0:
        f = True
        break

if f:
    print("No")
else:
    print("Yes")

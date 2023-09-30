n = int(input())

mid = n // 2
l, r = 0, n
for i in range(20):
    print("? {}".format(mid))
    m = int(input())
    if m == 0:
        l = mid
    if m == 1:
        r = mid

    mid = (l + r) // 2

    if r - l == 1:
        break

print("! {}".format(l))

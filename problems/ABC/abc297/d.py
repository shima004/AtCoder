s = input()

bx = s.index("B") + 1
by = s.rindex("B") + 1
rx = s.index("R") + 1
ry = s.rindex("R") + 1
k = s.index("K") + 1


if bx % 2 != by % 2:
    if rx < k and k < ry:
        print("Yes")
    else:
        print("No")
else:
    print("No")

x, y = map(int, input().split())
if (x - y) <= 0 and (x - y) >= -2:
    print("Yes")
    exit()

if (x - y) >= 0 and (x - y) <= 3:
    print("Yes")
    exit()

print("No")

n, m, h, k = map(int, input().split())
s = input()
items = [list(map(int, input().split())) for _ in range(m)]
items_dict = {str(i[0]) + "," + str(i[1]): 1 for i in items}

ans = "Yes"
x, y = 0, 0
for i in s:
    h -= 1
    if h < 0:
        ans = "No"
        break
    if i == "R":
        x += 1
    elif i == "L":
        x -= 1
    elif i == "U":
        y += 1
    elif i == "D":
        y -= 1

    if items_dict.get(str(x) + "," + str(y)) == 1 and h < k:
        h = k
        items_dict[str(x) + "," + str(y)] = 0

print(ans)

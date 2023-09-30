H, W = map(int, input().split())
cookies = [list(input()) for _ in range(H)]

while True:
    if len(cookies) == 0 or len(cookies[0]) == 0:
        break

    row = []
    for i in range(len(cookies)):
        c = cookies[i].count(cookies[i][0])
        if c == len(cookies[i]) and c > 1:
            row.append(i)

    col = []
    for j in range(len(cookies[0])):
        c = [cookies[i][j] for i in range(len(cookies))].count(cookies[0][j])
        if c == len(cookies) and c > 1:
            col.append(j)

    if len(row) == 0 and len(col) == 0:
        break

    for i in row[::-1]:
        cookies.pop(i)
    for j in col[::-1]:
        for i in range(len(cookies)):
            cookies[i].pop(j)

if len(cookies) == 0 or len(cookies[0]) == 0:
    print(0)
else:
    print(len(cookies) * len(cookies[0]))

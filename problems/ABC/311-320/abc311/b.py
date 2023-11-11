n, d = map(int, input().split())
s = [input() for _ in range(n)]

ans = 0
count = 0
for i in range(d):
    flag = True
    for j in range(n):
        if s[j][i] == "x":
            flag = False
            break
    if flag:
        count += 1
    else:
        ans = max(ans, count)
        count = 0

ans = max(ans, count)
print(ans)

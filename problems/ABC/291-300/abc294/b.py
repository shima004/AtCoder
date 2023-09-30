h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]


for i in range(h):
    ans = ""
    for j in a[i]:
        if j == 0:
            ans += "."
        else:
            ans += chr(64 + j)
    print(ans)

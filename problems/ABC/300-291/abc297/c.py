h, w = map(int, input().split())
for i in range(h):
    s = list(input())
    p = 0
    while p < (w - 1):
        if s[p] == "T" and s[p + 1] == "T":
            s[p] = "P"
            s[p + 1] = "C"
            p += 2
        else:
            p += 1
    print("".join(s))

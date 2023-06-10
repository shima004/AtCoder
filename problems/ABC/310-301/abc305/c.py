h, w = map(int, input().split())
s = [input() for _ in range(h)]

sh, eh, sw, ew = 1000, -1, 1000, -1

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            sh = min(sh, i)
            eh = max(eh, i)
            sw = min(sw, j)
            ew = max(ew, j)


s = [s[i][sw : ew + 1] for i in range(sh, eh + 1)]
ans = (0, 0)
for i in range(eh - sh + 1):
    for j in range(ew - sw + 1):
        if s[i][j] == ".":
            ans = (i, j)
            break
    else:
        continue
    break

print(ans[0] + 1 + sh, ans[1] + 1 + sw)

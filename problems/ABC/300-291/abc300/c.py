h, w = map(int, input().split())

c = [list(input()) for _ in range(h)]

crosses = [0 for i in range(min(h, w))]
for i in range(h):
    for j in range(w):
        if c[i][j] == "#":
            if (
                i + 1 < h
                and j + 1 < w
                and i - 1 >= 0
                and j - 1 >= 0
                and c[i + 1][j + 1] == "#"
                and c[i + 1][j - 1] == "#"
                and c[i - 1][j + 1] == "#"
                and c[i - 1][j - 1] == "#"
            ):
                for k in range(min(h, w)):
                    if i + k >= h or j + k >= w or c[i + k][j + k] != "#":
                        break
                crosses[k - 2] += 1


print(" ".join(map(str, crosses)))

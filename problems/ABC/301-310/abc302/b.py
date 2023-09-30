h, w = map(int, input().split())
s = [input() for _ in range(h)]

ans = 0

for i in range(h):
    for j in range(w):
        if i + 4 < h:
            if (
                s[i][j] == "s"
                and s[i + 1][j] == "n"
                and s[i + 2][j] == "u"
                and s[i + 3][j] == "k"
                and s[i + 4][j] == "e"
            ):
                ans = [(i, j), (i + 1, j), (i + 2, j), (i + 3, j), (i + 4, j)]
                break
        if i - 4 >= 0:
            if (
                s[i][j] == "s"
                and s[i - 1][j] == "n"
                and s[i - 2][j] == "u"
                and s[i - 3][j] == "k"
                and s[i - 4][j] == "e"
            ):
                ans = [(i, j), (i - 1, j), (i - 2, j), (i - 3, j), (i - 4, j)]
                break
        if j + 4 < w:
            if (
                s[i][j] == "s"
                and s[i][j + 1] == "n"
                and s[i][j + 2] == "u"
                and s[i][j + 3] == "k"
                and s[i][j + 4] == "e"
            ):
                ans = [(i, j), (i, j + 1), (i, j + 2), (i, j + 3), (i, j + 4)]
                break
        if j - 4 >= 0:
            if (
                s[i][j] == "s"
                and s[i][j - 1] == "n"
                and s[i][j - 2] == "u"
                and s[i][j - 3] == "k"
                and s[i][j - 4] == "e"
            ):
                ans = [(i, j), (i, j - 1), (i, j - 2), (i, j - 3), (i, j - 4)]
                break
        if i + 4 < h and j + 4 < w:
            if (
                s[i][j] == "s"
                and s[i + 1][j + 1] == "n"
                and s[i + 2][j + 2] == "u"
                and s[i + 3][j + 3] == "k"
                and s[i + 4][j + 4] == "e"
            ):
                ans = [
                    (i, j),
                    (i + 1, j + 1),
                    (i + 2, j + 2),
                    (i + 3, j + 3),
                    (i + 4, j + 4),
                ]
                break
        if i - 4 >= 0 and j - 4 >= 0:
            if (
                s[i][j] == "s"
                and s[i - 1][j - 1] == "n"
                and s[i - 2][j - 2] == "u"
                and s[i - 3][j - 3] == "k"
                and s[i - 4][j - 4] == "e"
            ):
                ans = [
                    (i, j),
                    (i - 1, j - 1),
                    (i - 2, j - 2),
                    (i - 3, j - 3),
                    (i - 4, j - 4),
                ]
                break
        if i + 4 < h and j - 4 >= 0:
            if (
                s[i][j] == "s"
                and s[i + 1][j - 1] == "n"
                and s[i + 2][j - 2] == "u"
                and s[i + 3][j - 3] == "k"
                and s[i + 4][j - 4] == "e"
            ):
                ans = [
                    (i, j),
                    (i + 1, j - 1),
                    (i + 2, j - 2),
                    (i + 3, j - 3),
                    (i + 4, j - 4),
                ]
                break
        if i - 4 >= 0 and j + 4 < w:
            if (
                s[i][j] == "s"
                and s[i - 1][j + 1] == "n"
                and s[i - 2][j + 2] == "u"
                and s[i - 3][j + 3] == "k"
                and s[i - 4][j + 4] == "e"
            ):
                ans = [
                    (i, j),
                    (i - 1, j + 1),
                    (i - 2, j + 2),
                    (i - 3, j + 3),
                    (i - 4, j + 4),
                ]
                break

for i in ans:
    print(i[0] + 1, i[1] + 1)

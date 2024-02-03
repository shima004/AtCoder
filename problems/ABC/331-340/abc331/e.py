def ans(N, M, L, main_dishes, side_dishes, bad):
    bad_set = set((c, d) for c, d in bad)
    sorted_main = sorted(
        enumerate(main_dishes, start=1), key=lambda x: x[1], reverse=True
    )
    sorted_side = sorted(
        enumerate(side_dishes, start=1), key=lambda x: x[1], reverse=True
    )

    ans = []
    for side_i, side_p in sorted_side:
        for main_i, main_p in sorted_main:
            if (main_i, side_i) not in bad_set:
                ans.append(main_p + side_p)
                break

    for main_i, main_p in sorted_main:
        for side_i, side_p in sorted_side:
            if (main_i, side_i) not in bad_set:
                ans.append(main_p + side_p)
                break

    if ans:
        return max(ans)

    return -1


n, m, l = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c, d = [], []
for i in range(l):
    _c, _d = map(int, input().split())
    c.append(_c)
    d.append(_d)

print(ans(n, m, l, a, b, zip(c, d)))

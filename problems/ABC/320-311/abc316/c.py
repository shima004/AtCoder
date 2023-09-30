n, d, p = map(int, input().split())
f = list(map(int, input().split()))
f_sorted = sorted(f, reverse=True)
ans = 0
for i in range(0, n, d):
    f_cost = sum(f_sorted[i : i + d])
    if f_cost > p:
        ans += p
        f_sorted[i : i + d] = [0] * d

print(ans + sum(f_sorted))

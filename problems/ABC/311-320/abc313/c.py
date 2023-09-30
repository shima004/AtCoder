n = int(input())
a = list(map(int, input().split()))
sorted_a = sorted(a)

s = sum(a)
p, r = s // n, s % n

ans = 0
r = n - r
for i in range(n):
    if r > 0:
        ans += abs(sorted_a[i] - p)
        r -= 1
    else:
        ans += abs(sorted_a[i] - (p + 1))

print(ans // 2)

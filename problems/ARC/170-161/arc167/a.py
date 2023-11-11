n, m = map(int, input().split())
a = list(map(int, input().split()))
sorted_a = sorted(a, reverse=True)
ans = 0
for i in range((m * 2) - n):
    ans += sorted_a[i] ** 2
sorted_a = sorted_a[(m * 2) - n :]

for i in range(len(sorted_a) // 2):
    ans += (sorted_a[i] + sorted_a[len(sorted_a) - i - 1]) ** 2

print(ans)

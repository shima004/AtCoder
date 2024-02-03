n = int(input())
a = list(map(int, input().split()))
max_a = max(a)
ans = 0
for i in range(n):
    if a[i] == max_a:
        continue
    else:
        ans = max(ans, a[i])

print(ans)

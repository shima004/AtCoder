n, x = map(int, input().split())
s = list(map(int, input().split()))
ans = 0
for i in s:
    if i <= x:
        ans += i

print(ans)

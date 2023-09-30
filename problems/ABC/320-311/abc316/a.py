n, m, p = map(int, input().split())

ans = 1
n = n - m
ans += n // p
print(ans)

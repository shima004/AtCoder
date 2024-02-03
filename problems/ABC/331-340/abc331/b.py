n, s, m, l = map(int, input().split())
dp = [10**10] * (n + 20)
dp[0] = 0

for i in range(1, n + 20):
    if i >= 6:
        dp[i] = min(dp[i], dp[i - 6] + s)
    if i >= 8:
        dp[i] = min(dp[i], dp[i - 8] + m)
    if i >= 12:
        dp[i] = min(dp[i], dp[i - 12] + l)

print(min(dp[n : n + 20]))

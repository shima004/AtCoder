x, y, z = map(int, input().split())
s = input()
split = []

dp = [[10**15, 10**15] for _ in range(len(s) + 1)]
dp[0][0] = 0

for i in range(len(s)):
    _s = 0 if s[i] == "a" else 1
    for j in range(2):
        v = dp[i][j]
        if _s == j:
            dp[i + 1][j] = min(dp[i + 1][j], v + x)
            dp[i + 1][j ^ 1] = min(dp[i + 1][j ^ 1], v + z + y)
        else:
            dp[i + 1][j] = min(dp[i + 1][j], v + y)
            dp[i + 1][j ^ 1] = min(dp[i + 1][j ^ 1], v + z + x)

print(min(dp[len(s)]))

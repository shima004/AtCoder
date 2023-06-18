n = int(input())
x, y = [], []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

dp = [[0, 0] for _ in range(n + 1)]

for i in range(n):
    if x[i] == 0:
        dp[i + 1][0] = max(dp[i][0], dp[i][1] + y[i], dp[i][0] + y[i])
        dp[i + 1][1] = dp[i][1]
    else:
        dp[i + 1][1] = max(dp[i][0] + y[i], dp[i][1])
        dp[i + 1][0] = dp[i][0]

print(max(dp[n][0], dp[n][1]))

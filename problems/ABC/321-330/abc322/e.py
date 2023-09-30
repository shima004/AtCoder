n, k, p = map(int, input().split())
c = []
a = []
for _ in range(n):
    s = list(map(int, input().split()))
    c.append(s[0])
    a.append(s[1:])
# n, k, p = 100, 5, 5

# import random

# c = [random.randint(1, 10**9) for _ in range(n)]
# a = [[random.randint(0, p) for _ in range(k)] for _ in range(n)]

import collections

dp = [collections.defaultdict(lambda: 10**18) for _ in range(n + 1)]
dp[0][",".join(["0"] * k)] = 0

for i in range(n):
    min_ans = 10**18
    for key, v in dp[i].items():
        next_k = key.split(",")
        for j in range(k):
            next_k[j] = str(min(int(next_k[j]) + a[i][j], p))
        next_k = ",".join(next_k)
        dp[i + 1][next_k] = min(dp[i + 1][next_k], v + c[i])
        dp[i + 1][key] = min(dp[i + 1][key], v)

ans = []
for key, v in dp[n].items():
    key = key.split(",")
    if all([int(i) >= p for i in key]):
        ans.append((v, key))

print(min(ans)[0] if ans else -1)

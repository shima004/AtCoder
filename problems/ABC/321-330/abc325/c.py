import sys

sys.setrecursionlimit(10**6)

h, w = map(int, input().split())
s = [input() for _ in range(h)]
sarched = [[False for _ in range(w)] for _ in range(h)]


def dfs(i, j):
    if i < 0 or j < 0 or i >= h or j >= w:
        return 0
    if sarched[i][j]:
        return 0
    if s[i][j] == ".":
        return 0
    sarched[i][j] = True
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)
    dfs(i + 1, j + 1)
    dfs(i + 1, j - 1)
    dfs(i - 1, j + 1)
    dfs(i - 1, j - 1)


ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == "#" and not sarched[i][j]:
            dfs(i, j)
            ans += 1

print(ans)

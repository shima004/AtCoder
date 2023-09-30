n, m = map(int, input().split())
friends = [[0] * n for _ in range(n)]

for _ in range(m):
    a = list(map(int, input().split()))
    a = [i - 1 for i in a]
    for i in range(1, len(a)):
        friends[a[i - 1]][a[i]] = 1
        friends[a[i]][a[i - 1]] = 1

for i in range(n):
    friends[i][i] = 1


ans = 0
for i in range(n):
    for j in friends[i]:
        if j == 0:
            ans += 1

print(ans // 2)

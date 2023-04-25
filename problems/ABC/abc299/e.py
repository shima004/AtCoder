from collections import defaultdict

n, m = map(int, input().split())
v = [[] for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    v[a].append(b)
    v[b].append(a)

distance = [[-1] * n for i in range(n)]


def bfs(start):
    q = [start]
    distance[start][start] = 0
    while q:
        now = q.pop(0)
        for i in v[now]:
            if distance[start][i] == -1:
                distance[start][i] = distance[start][now] + 1
                q.append(i)


for i in range(n):
    bfs(i)

k = int(input())
pd = [list(map(int, input().split())) for i in range(k)]

ans = [-1 for i in range(n)]
for i in pd:
    p, d = i[0] - 1, i[1]
    for j, item in enumerate(distance[p]):
        if item < d:
            ans[j] = 0

for i in range(n):
    if ans[i] == -1:
        ans[i] = 1

a = "Yes"
for i in pd:
    p, d = i[0] - 1, i[1]
    flag = False
    for j, item in enumerate(distance[p]):
        if item == d and ans[j] == 1:
            flag = True

    if not flag:
        a = "No"

print(a)
if a == "Yes":
    print("".join(map(str, ans)))

n, m = map(int, input().split())
a = []
b = []
x = []
y = []
path = {i: [] for i in range(n)}
dist = {}
for i in range(m):
    a_, b_, x_, y_ = map(int, input().split())
    a.append(a_)
    b.append(b_)
    path[a_ - 1].append(b_ - 1)
    path[b_ - 1].append(a_ - 1)
    x.append(x_)
    y.append(y_)
    dist[(a_ - 1, b_ - 1)] = [x_, y_]
    dist[(b_ - 1, a_ - 1)] = [-x_, -y_]

ans = [[] for _ in range(n)]
q = [0]
ans[0] = [0, 0]
while q:
    now = q.pop()
    nexts = path[now]
    for next in nexts:
        if ans[next]:
            continue
        d = dist[(now, next)]
        ans[next] = [ans[now][0] + d[0], ans[now][1] + d[1]]
        q.append(next)

for i in range(n):
    if not ans[i]:
        print("undecidable")
    else:
        print(ans[i][0], ans[i][1])

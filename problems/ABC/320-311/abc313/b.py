n, m = map(int, input().split())
path = []
for i in range(m):
    path.append(list(map(int, input().split())))

s = [0] * n
for i in range(m):
    s[path[i][1] - 1] += 1

if s.count(0) == 1:
    print(s.index(0) + 1)
else:
    print(-1)

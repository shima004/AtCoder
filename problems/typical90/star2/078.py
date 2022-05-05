n, m = map(int, input().split())
path = [0 for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a, b = (a, b) if a < b else (b, a)
    path[b-1] += 1

print(path.count(1))

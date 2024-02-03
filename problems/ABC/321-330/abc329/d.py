n, m = map(int, input().split())
a = list(map(int, input().split()))

v = [0] * (n + 1)
top = 1

for i in range(m):
    c = a[i]
    v[c] += 1
    if v[c] > v[top] or (v[c] == v[top] and c < top):
        top = c
    print(top)

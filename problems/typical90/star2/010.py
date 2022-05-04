N = int(input())
a, b = [0]*(N + 2), [0]*(N + 2)
for i in range(N):
    c, p = map(int, input().split())
    if c == 1:
        a[i] += p + (0 if i == 0 else a[i-1])
        b[i] = 0 if i == 0 else b[i-1]
    else:
        b[i] += p + (0 if i == 0 else b[i-1])
        a[i] = 0 if i == 0 else a[i-1]

for i in range(int(input())):
    l, r = map(int, input().split())
    print(a[r-1] - a[l-2], b[r-1] - b[l-2])

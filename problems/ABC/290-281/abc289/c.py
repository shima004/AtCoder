import itertools

n, m = map(int, input().split())
a = []
for i in range(m):
    length = int(input())
    arr = list(map(int, input().split()))
    b = 0
    for j in arr:
        b += 2**(j-1)
    a.append(b)

ans = 0
c = list(itertools.product([0, 1], repeat=m))
while len(c) >= 1:
    index = c.pop()
    t = 0
    for i in range(m):
        if index[i] == 1:
            t |= a[i]
    if t == 2**n-1:
        ans += 1
print(ans)

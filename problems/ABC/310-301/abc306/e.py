import collections

n, k, q = map(int, input().split())
a = [0] * n
num = collections.defaultdict(int)
num[0] = n
center = 0

for i in range(q):
    x, y = map(int, input().split())
    x -= 1

    num[a[x]] -= 1
    a[x] = y
    num[y] += 1

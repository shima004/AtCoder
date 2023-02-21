import collections

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = collections.defaultdict(int)
for i in a:
    b[i] += 1

ans = 0
num = 0
for i in range(k):
    num += b[i]
    if b[i] != 0 and i == (k - 1):
        ans = i + 1
        break
    if b[i] == 0:
        ans = i
        break

print(ans)

import itertools

n = int(input())
a = list(map(int, input().split()))
sorted_a = sorted(a)
gr = itertools.groupby(sorted_a)

ans = 0
for key, group in gr:
    ans += len(list(group)) // 2

print(ans)

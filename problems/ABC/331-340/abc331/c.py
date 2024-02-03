n = int(input())
a = list(map(int, input().split()))
sorted_a = sorted(a, reverse=True)
prefix_sum = [0] * (n + 1)
_sum = sum(a)
ans = [_sum] * (10**6 + 10)
for i in range(1, (10**6) + 10):
    ans[i] = ans[i - 1]
    while sorted_a and sorted_a[-1] == i:
        ans[i] -= sorted_a.pop()

s = []
for i in range(n):
    s.append(ans[a[i]])

print(" ".join(map(str, s)))

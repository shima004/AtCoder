n = int(input())
a = list(map(int, input().split()))
sorted_a = sorted(a)
big = sorted_a[(n // 2) + 1 :]
small = sorted_a[: (n // 2) + 1]


ans = "Yes"
for i in range(len(big)):
    if big[i] <= small[i] or big[i] <= small[i + 1]:
        ans = "No"
        break
print(ans)

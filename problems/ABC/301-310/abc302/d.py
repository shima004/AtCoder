n, m, d = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sorted_a = sorted(a, reverse=True)
sorted_b = sorted(b, reverse=True)


a_i = 0
b_i = 0
while True:
    if a_i == n or b_i == m:
        break
    if abs(sorted_a[a_i] - sorted_b[b_i]) <= d:
        break
    if sorted_a[a_i] > sorted_b[b_i]:
        a_i += 1
    else:
        b_i += 1


if a_i == n or b_i == m:
    print(-1)
elif abs(sorted_a[a_i] - sorted_b[b_i]) <= d:
    print(sorted_a[a_i] + sorted_b[b_i])
else:
    print(-1)

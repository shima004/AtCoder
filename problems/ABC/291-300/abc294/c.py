n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_ans = []
b_ans = []

a_i, b_i = 0, 0
for i in range(n + m):
    if a_i == n and b_i == m:
        break
    if a_i == n:
        b_ans.append(i + 1)
        b_i += 1
    elif b_i == m:
        a_ans.append(i + 1)
        a_i += 1
    elif a[a_i] < b[b_i]:
        a_ans.append(i + 1)
        a_i += 1
    else:
        b_ans.append(i + 1)
        b_i += 1

print(" ".join(map(str, a_ans)))
print(" ".join(map(str, b_ans)))

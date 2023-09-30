n = int(input())
a = list(map(int, input().split()))

ans = ""
for i in range(n - 1):
    a_one = a[i]
    a_two = a[i + 1]
    if a_one > a_two:
        for j in range(a_one, a_two, -1):
            ans += " " + str(j)
    elif a_one < a_two:
        for j in range(a_one, a_two):
            ans += " " + str(j)

ans += " " + str(a[-1])
ans = ans[1:]

print(ans)

n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = []
c = 0
index = m - 1
for i in range(n + 1, 0, -1):
    if a[index] == i:
        c = 0
        index -= 1
    ans.append(c)
    c += 1

reversed_ans = ans[::-1]
reversed_ans = reversed_ans[:-1]
for i in reversed_ans:
    print(i)

n = int(input())
a = list(map(int, input().split()))
for i in range(len(a)):
    a[i] -= 1
flag = [0] * (n)
center = [[0, i] for i in range(n)]


for i, v in enumerate(a):
    if flag[v] == 1:
        center[v][0] = i
        flag[v] = 2
    else:
        flag[v] = 1

center.sort(key=lambda x: x[0])
for i in center:
    print(i[1] + 1, end=" ")
print()

n = int(input())
step = list(map(int, input().split()))
m = int(input())
trap = list(map(int, input().split()))
x = int(input())

a = [0] * (x + 1)
a[0] = 1
b = [0] * (x + 1)
for i in trap:
    b[i] = 1

for i in range(x):
    if a[i] == 0 or b[i] == 1:
        continue
    for j in step:
        if i + j <= x:
            a[i + j] = 1

if a[x] == 1:
    print("Yes")
else:
    print("No")

n = int(input())

for i in range(n, 920):
    a = str(i)
    if int(a[0]) * int(a[1]) == int(a[2]):
        print(i)
        exit()

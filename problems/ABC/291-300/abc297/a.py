n, d = map(int, input().split())
t = list(map(int, input().split()))

b = -1000000000000000000
for i in range(len(t)):
    if t[i] - b <= d:
        print(t[i])
        exit()
    b = t[i]
print("-1")

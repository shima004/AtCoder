q = int(input())

X = []
for i in range(q):
    t, x = map(int, input().split())
    if t == 1:
        X.insert(0, x)
    elif t == 2:
        X.append(x)
    elif t == 3:
        print(X[x-1])

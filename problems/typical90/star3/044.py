from sys import stdin


N, Q = map(int, input().split())
A = list(map(int, stdin.readline().split()))
shift = 0
for i in range(Q):
    t, x, y = map(int, stdin.readline().split())
    if t == 1:
        x = x - (shift % N)
        y = y - (shift % N)
        tmp = A[x-1]
        A[x-1] = A[y-1]
        A[y-1] = tmp
    elif t == 2:
        shift += 1
    else:
        x = x - (shift % N)
        print(A[x-1])

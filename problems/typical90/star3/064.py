from sys import stdin


N, Q = map(int, input().split())
A = list(map(int, stdin.readline().split()))
a_sub = [0] * N
ans = 0
for i in range(N-1):
    a_sub[i] = A[i+1] - A[i]
    ans += abs(a_sub[i])

for i in range(Q):
    l, r, v = map(int, input().split())
    l -= 1
    r -= 1
    before = abs(a_sub[l-1]) + abs(a_sub[r])
    if r < N-1:
        a_sub[r] -= v
    if l > 0:
        a_sub[l-1] += v
    else:
        if r == 0:
            a_sub[r] += v
        a_sub[l] += v
    after = abs(a_sub[l-1]) + abs(a_sub[r])
    ans += after - before
    print(ans)

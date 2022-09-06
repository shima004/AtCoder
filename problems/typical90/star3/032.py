import itertools


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
B = [list(map(int, input().split())) for _ in range(M)]
runner = itertools.permutations(range(1, N+1), N)
ans = 10**9


for j, a in enumerate(runner):
    time = 0
    for i in range(N):
        if i != (N-1) and ([a[i], a[i+1]] in B or [a[i+1], a[i]] in B):
            time += 10**9
            break
        time += A[a[i]-1][i]
    ans = min(ans, time)
print(-1 if ans == 10**9 else ans)

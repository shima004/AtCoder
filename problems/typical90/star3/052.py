N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
ans = 1
for i in A:
    ans *= sum(i)

print(ans % (10**9+7))

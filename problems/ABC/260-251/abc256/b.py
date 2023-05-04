N = int(input())
A = list(map(int, input().split()))
m = [0] * (N)
m[N-1] = A[N-1]
for i in range(N-1, 0, -1):
    m[i-1] = A[i-1] + m[i]

ans = 0
for item in m:
    if item >= 4:
        ans += 1
print(ans)

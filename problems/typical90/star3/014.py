from sys import stdin


N = int(input())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))
A = sorted(A)
B = sorted(B)
ans = 0
for i in range(N):
    ans += abs(A[i] - B[i])
print(ans)

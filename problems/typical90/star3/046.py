from sys import stdin


N = int(input())
A = list(map(lambda x: x % 46, map(int, stdin.readline().split())))
B = list(map(lambda x: x % 46, map(int, stdin.readline().split())))
C = list(map(lambda x: x % 46, map(int, stdin.readline().split())))
A_count = [0] * 46
B_count = [0] * 46
C_count = [0] * 46
ans = 0
for i in range(N):
    A_count[A[i]] += 1
    B_count[B[i]] += 1
    C_count[C[i]] += 1
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k) % 46 == 0:
                ans += A_count[i] * B_count[j] * C_count[k]
print(ans)

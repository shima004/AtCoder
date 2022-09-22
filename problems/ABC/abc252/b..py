from sys import stdin


N, K = map(int, input().split())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))
a_max = max(A)
a_maxarg = [i + 1 for i in range(N) if A[i] == a_max]
for i in B:
    if i in a_maxarg:
        print("Yes")
        exit()
print("No")

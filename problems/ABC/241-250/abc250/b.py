N, A, B = map(int, input().split())
ans = [[0]*(B*N) for _ in range(A*N)]
for i in range(A*N):
    for j in range(B*N):
        if ((j // B) + (i // A)) % 2 == 0:
            ans[i][j] = "."
        else:
            ans[i][j] = "#"

for i in ans:
    for j in i:
        print(j, end="")
    print()

N = int(input())
A, B, C = list(map(int, input().split()))
A, B, C = sorted([A, B, C], reverse=True)

limit = 9999
ans = limit
for i in range(limit):
    for j in range(limit - i):
        if (N - ((A * i) + (B * j))) < 0:
            break
        if ((N - ((A * i) + (B * j))) % C) == 0:
            k = (N - ((A * i) + (B * j))) // C
            ans = min(ans, i + j + k)
print(ans)

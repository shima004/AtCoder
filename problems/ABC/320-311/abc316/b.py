n = int(input())
s = [[0 for _ in range(100)] for _ in range(100)]

for i in range(n):
    a, b, c, d = map(int, input().split())
    for j in range(a, b):
        for k in range(c, d):
            s[j][k] = 1

print(sum([s[i][j] for i in range(100) for j in range(100)]))

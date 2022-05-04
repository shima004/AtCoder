from sys import stdin

h, w = map(int, input().split())
x, y = [0]*h, [0]*w

field = [list(map(int, stdin.readline().split())) for _ in range(h)]

for i in range(h):
    for j in range(w):
        x[i] += field[i][j]
        y[j] += field[i][j]

for i in range(h):
    for j in range(w):
        print(x[i]+y[j] - field[i][j], end=' ')
    print()

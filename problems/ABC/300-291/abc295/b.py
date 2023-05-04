r, c = map(int, input().split())
f = [list(input()) for _ in range(r)]
bombs = []

for i in range(r):
    for j in range(c):
        if f[i][j] != "." and f[i][j] != "#":
            bombs.append([i, j, int(f[i][j])])

for bomb in bombs:
    x, y, n = bomb
    for i in range(x - n, x + n + 1):
        for j in range(y - n, y + n + 1):
            if 0 <= i < r and 0 <= j < c:
                if abs(x - i) + abs(y - j) <= n:
                    f[i][j] = "."

for i in range(r):
    print("".join(map(str, f[i])))

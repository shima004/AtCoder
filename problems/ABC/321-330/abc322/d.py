p = [input() for _ in range(12)]

# ポリオミノの形状を表す配列
polyominoes = []
polyominoes.append([list(p[i]) for i in range(4)])
polyominoes.append([list(p[i]) for i in range(4, 8)])
polyominoes.append([list(p[i]) for i in range(8, 12)])


def rotate(polyomino):
    return list(zip(*polyomino[::-1]))


def is_inrange(i, j, i_max, j_max):
    return 0 <= i < i_max and 0 <= j < j_max


def put(field, mino, x, y):
    for k in range(4):
        for l in range(4):
            if mino[k][l] == "#":
                if not is_inrange(x + k, y + l, 4, 4):
                    return False
                if field[x + k][y + l] == "#":
                    return False
    for k in range(4):
        for l in range(4):
            if mino[k][l] == "#":
                field[x + k][y + l] = "#"
    return True


def dfs(i, field, polyominoes):
    if i == 3:
        return all(all(f == "#" for f in field[j]) for j in range(4))
    for j in range(-3, 4):
        for k in range(-3, 4):
            copy = [f[:] for f in field]
            if put(copy, polyominoes[i], j, k):
                copy = [f[:] for f in copy]
                if dfs(i + 1, copy, polyominoes):
                    return True
    return False


flag = False
for i in range(4):
    for j in range(4):
        field = [["."] * 4 for _ in range(4)]
        flag = dfs(0, field, polyominoes) or flag
        polyominoes[1] = rotate(polyominoes[1])
    polyominoes[2] = rotate(polyominoes[2])

if flag:
    print("Yes")
else:
    print("No")

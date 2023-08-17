def is_valid_move(x, y, H, W):
    return 0 <= x < H and 0 <= y < W


def dfs(grid, x, y, H, W, pattern, idx):
    if x == H - 1 and y == W - 1:
        return True

    if grid[x][y] != pattern[idx]:
        return False

    temp = grid[x][y]
    grid[x][y] = "."

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if is_valid_move(nx, ny, H, W) and grid[nx][ny] != ".":
            if dfs(grid, nx, ny, H, W, pattern, (idx + 1) % 5):
                return True

    grid[x][y] = temp

    return False


def has_valid_path(grid, H, W):
    pattern = "snuke"

    return dfs(grid, 0, 0, H, W, pattern, 0)


H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

if has_valid_path(grid, H, W):
    print("Yes")
else:
    print("No")

n, q = map(int, input().split())
p = [list(input()) for i in range(n)]

grid = [[0] * n for _ in range(n)]
_sum = 0
for i in range(n):
    for j in range(n):
        if p[i % n][j % n] == "B":
            grid[i][j] = 1
            _sum += 1

cumsum = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        cumsum[i + 1][j + 1] = (
            cumsum[i + 1][j] + cumsum[i][j + 1] - cumsum[i][j] + grid[i][j]
        )

print(cumsum)


def count_full_cycles(start, end, period):
    start_adjusted = start if start % period == 0 else start + period - start % period
    end_adjusted = end if end % period == 0 else end - end % period
    print(start_adjusted, end_adjusted)
    if start_adjusted >= end_adjusted:
        return 0
    return (end_adjusted - start_adjusted) // period


for i in range(q):
    a, b, c, d = map(int, input().split())

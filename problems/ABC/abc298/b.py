import numpy as np

n = int(input())
a = np.array([list(map(int, input().split())) for i in range(n)])
b = np.array([list(map(int, input().split())) for i in range(n)])


def check(a, b):
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 and b[i][j] == 0:
                return False
    return True


def rotate(n):
    tmp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[i][j] = a[i][j]
    for i in range(n):
        for j in range(n):
            a[i][j] = tmp[n - j - 1][i]


for i in range(4):
    rotate(n)
    if check(a, b):
        print("Yes")
        exit()
print("No")

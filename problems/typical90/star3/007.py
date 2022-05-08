from sys import stdin


def binary_search(a, x, boolfunc):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if boolfunc(a[mid], x):
            right = mid - 1
        else:
            left = mid + 1
    if (left != 0 and left != len(a)):
        left = left if abs(a[left] - x) < abs(a[left-1] - x) else left - 1
    if (left == len(a)):
        left = left - 1
    return left


N = int(input())
A = list(map(int, stdin.readline().split()))
A = sorted(A)
Q = int(input())
for i in range(Q):
    b = int(input())
    print(abs(b - A[binary_search(A, b, lambda mid, x: mid > x)]))

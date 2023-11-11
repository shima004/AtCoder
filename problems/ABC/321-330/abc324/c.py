def ans(N, M, A):
    A.sort()
    left = 0
    max_presents = 0
    for right in range(N):
        while A[right] - A[left] >= M:
            left += 1
        max_presents = max(max_presents, right - left + 1)
    return max_presents


N, M = map(int, input().split())
A = list(map(int, input().split()))
print(ans(N, M, A))

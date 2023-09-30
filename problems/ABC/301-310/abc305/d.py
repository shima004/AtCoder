def lower_bound(arr, x):
    l = 0
    r = len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return l


def upper_bound(arr, x):
    l = 0
    r = len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] <= x:
            l = m + 1
        else:
            r = m
    return l


n = int(input())
a = list(map(int, input().split()))
a_cumulative_sum = [0] * (n)
q = int(input())


for i in range(n):
    if i % 2 == 1:
        a_cumulative_sum[i] = a_cumulative_sum[i - 1] + a[i + 1] - a[i]
    else:
        a_cumulative_sum[i] = a_cumulative_sum[i - 1]


for i in range(q):
    l, r = map(int, input().split())
    l_i = lower_bound(a, l)
    r_i = upper_bound(a, r)
    ans = 0

    if l_i % 2 == 0:
        ans += a[l_i] - l
        l_i += 1

    if r_i % 2 == 0:
        ans += r - a[r_i - 1]
        r_i -= 1

    if l_i == 0:
        l_i = 1

    ans += a_cumulative_sum[r_i - 1] - a_cumulative_sum[l_i - 1]

    print(ans)

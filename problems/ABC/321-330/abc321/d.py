import itertools

n, m, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b_sorted = sorted(b)
b_cumulative = list(itertools.accumulate(b_sorted))


def bin_search(b, x):
    l = 0
    r = len(b) - 1
    while l <= r:
        mid = (l + r) // 2
        if b[mid] == x:
            return mid
        elif b[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return l


ans = 0
for i in a:
    d = p - i
    index = bin_search(b_sorted, d)
    if index == 0:
        ans += p * m
    else:
        ans += (i * index) + b_cumulative[index - 1] + (p * (m - index))

print(ans)

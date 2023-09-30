import collections


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


w, h = map(int, input().split())
n = int(input())
strawberry = []
for i in range(n):
    x, y = map(int, input().split())
    strawberry.append([x, y])

a_n = int(input())
a = list(map(int, input().split()))
b_n = int(input())
b = list(map(int, input().split()))

place = collections.defaultdict(int)

for s in strawberry:
    x = lower_bound(a, s[0])
    y = lower_bound(b, s[1])
    place[(x, y)] += 1

_min = 10**18
_max = 0

if len(place) < (a_n + 1) * (b_n + 1):
    _min = 0

for k, v in place.items():
    if v == 0:
        continue
    _min = min(_min, v)
    _max = max(_max, v)

print(_min, _max)

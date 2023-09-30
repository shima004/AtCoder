n, x = map(int, input().split())
a = list(map(int, input().split()))
a_sorted = sorted(a)
s = sum(a) - a_sorted[0] - a_sorted[-1]
_min = min(a)
_max = max(a)
diff = x - s
if diff < 0:
    print(0)
elif diff > 100:
    print(-1)
else:
    if diff <= _min:
        print(0)
    elif diff > _max:
        print(-1)
    else:
        print(diff)

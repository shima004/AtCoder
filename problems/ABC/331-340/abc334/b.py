a, m, l, r = map(int, input().split())

if l > a:
    start = a + ((l - a + m - 1) // m) * m
elif l < a:
    start = a - ((a - l) // m) * m
else:
    start = a

if r > a:
    end = a + ((r - a) // m) * m
elif r < a:
    end = a - ((a - r + m - 1) // m) * m
else:
    end = a

if start > r or end < l:
    print(0)
else:
    print((end - start) // m + 1)

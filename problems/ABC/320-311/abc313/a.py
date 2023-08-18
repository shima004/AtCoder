n = int(input())
p = list(map(int, input().split()))
if n == 1:
    print(0)
    exit()

p_max = max(p[1:-1])
p = p[0]
if p_max < p:
    print(0)
elif p_max == p:
    print(1)
else:
    print(p_max - p + 1)

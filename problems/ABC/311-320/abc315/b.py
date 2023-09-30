m = int(input())
d = list(map(int, input().split()))
d_s = [0]
for i in range(1, m + 1):
    d_s.append(d_s[i - 1] + d[i - 1])

mid = (sum(d) + 1) / 2

for i in range(1, m + 1):
    if d_s[i] >= mid:
        print("{} {}".format(i, int(d[i - 1] - (d_s[i] - mid))))
        exit()

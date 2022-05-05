N, P, Q = map(int, input().split())

a = list(map(lambda x: x % P, map(int, input().split())))
count = 0

for i in range(0, N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            for l in range(k + 1, N):
                for m in range(l + 1, N):
                    v = (a[i] * a[j] * a[k] * a[l] * a[m]) % P
                    if v == Q:
                        count += 1

print(count)

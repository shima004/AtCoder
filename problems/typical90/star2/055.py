import itertools


N, P, Q = map(int, input().split())

a = list(map(lambda x: x % P, map(int, input().split())))

count = 0
c = itertools.combinations(a, 5)
for item in c:
    if sum(item) % P == Q:
        count += 1
print(count)

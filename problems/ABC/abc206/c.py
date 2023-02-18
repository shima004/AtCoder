import collections
import math

n = int(input())
a = [int(x) for x in input().split()]
b = collections.defaultdict(int)
for i in a:
    b[i] += 1

com = math.comb(n, 2)

for item in b.values():
    com -= math.comb(item, 2)

print(com)

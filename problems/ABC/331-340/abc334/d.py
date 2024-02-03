from bisect import bisect_right
from itertools import accumulate

n, q = map(int, input().split())
r = list(map(int, input().split()))
query = [int(input()) for _ in range(q)]

sorted_r = sorted(r)
acc = list(accumulate(sorted_r))

for i in query:
    ans = bisect_right(acc, i)
    print(ans)

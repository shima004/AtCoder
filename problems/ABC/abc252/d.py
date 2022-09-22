import collections
from ctypes.wintypes import PINT


N = int(input())
A = list(map(int, input().split()))
A_same = [len(collections.Counter(A[i:])) for i in range(N)]
for i in range(N):
    print(A_same[i])

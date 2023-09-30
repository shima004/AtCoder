import numpy as np
n = int(input())
a = list(map(int, input().split()))
a = list(np.argsort(a))
print(a[-2]+1)

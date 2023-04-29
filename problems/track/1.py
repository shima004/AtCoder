import collections
import itertools
import sys

import numpy as np


def step1(a, b):
    print(sum(b)-sum(a))


def divable(diff, x) -> int:
    div = diff % x
    n = [0] * x
    for i in div:
        n[i] += 1
    n = list(itertools.accumulate(n))
    val = 0
    for i in range(x-1, 0, -1):
        print(i, n[i], val)
        if val != 0:
            if n[i] != val:
                return i+1
        elif n[i] >= i:
            val = i
    return 1


def step2(a, b, x, y):
    diff = np.array(sorted(b-a))
    if len(diff) <= x:
        c = divable(diff, x)
        ans = c
        diff = np.clip(diff-c, 0, None)
        print(diff, ans)
        for i in diff:
            # 切り上げ
            ans += -(-i // y)
        print(ans)
    else:
        v = diff[-x-1]
        print(v)
        remain = diff[-x:] - v
        div = remain % x
        print(div)


def step3(a, b, x, y):
    pass


if __name__ == '__main__':
    readline = sys.stdin.readline
    step = int(readline())
    n, x, y = map(int, readline().split())
    a, b = np.zeros(n, dtype=np.int64), np.zeros(n, dtype=np.int64)
    for i in range(n):
        a[i], b[i] = map(int, readline().split())

    if step == 1:
        step1(a, b)
    elif step == 2:
        step2(a, b, x, y)
    elif step == 3:
        pass
    else:
        pass

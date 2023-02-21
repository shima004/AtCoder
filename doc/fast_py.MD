# より早い書き方

# 1. stdin

```
from sys import stdin
readline = stdin.readline
A, B = map(int, readline().split())
xyzs = [list(map(int, stdin.readline().split())) for _ in range(n)]
ss = [stdin.readline()[:-1] for _ in range(n)]
```

[link](https://qiita.com/c-yan/items/dbf2838cdd89864ef5ac#%E9%AB%98%E9%80%9F%E5%8C%96)

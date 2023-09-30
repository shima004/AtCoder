from collections import defaultdict


class UnionFind:
    def __init__(self, n) -> None:
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i in range(self.n) if self.parents[i] < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group = defaultdict(list)
        for i in self.roots():
            group[i] = self.members(i)
        return group

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


n, m = map(int, input().split())
s = [input() for _ in range(n)]
alpha = [[0] * 26 for _ in range(n)]

for i in range(n):
    for j in range(m):
        alpha[i][ord(s[i][j]) - ord("a")] += 1

d = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        distance = 0
        for k in range(26):
            distance += abs(alpha[i][k] - alpha[j][k])
        if distance == 2:
            d[i][j] = 1

uf = UnionFind(n)

for i in range(n):
    for j in range(n):
        if d[i][j] == 1:
            uf.union(i, j)

if uf.group_count() == 1:
    print("Yes")
else:
    print("No")

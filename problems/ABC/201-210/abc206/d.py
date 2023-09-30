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
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


n = int(input())
a = [int(i) for i in input().split()]
uf = UnionFind(2 * 10 ** 5 + 1)

for i in range(n // 2):
    if a[i] != a[-i - 1]:
        uf.union(a[i], a[-i - 1])

ans = 0

for i in uf.roots():
    ans += uf.size(i) - 1

print(ans)

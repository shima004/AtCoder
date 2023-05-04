from collections import defaultdict
from sys import stdin


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


def main():
    n, m = map(int, input().split())

    uf = UnionFind(n)

    readline = stdin.readline
    path = [list(map(int, readline().split())) for _ in range(m)]

    min_path = 0

    for i in path:
        if uf.same(i[0]-1, i[1]-1):
            min_path += 1
        else:
            uf.union(i[0]-1, i[1]-1)

    print(min_path)


if __name__ == '__main__':
    main()

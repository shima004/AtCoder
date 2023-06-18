class SegmentTree:
    # https://qiita.com/R_olldIce/items/32cbf5bc3ffb2f84a898
    def __init__(self, op, e, n):
        self.n = len(n) if isinstance(n, list) else n
        self.op = op
        self.e = e
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [e for _ in range(2 * self.size)]
        if isinstance(n, list):
            self.d[self.size : self.size + self.n] = n
        [self._update(i) for i in reversed(range(1, self.size))]

    def __repr__(self):
        l, r = 1, 2
        res = []
        while r <= 2 * self.size:
            res.append(f"{self.d[l: r]}")
            l, r = r, r << 1
        return "\n".join(res)

    def set(self, p, x):  # O(log n)
        p += self.size
        self.d[p] = x
        [self._update(p >> i) for i in range(1, self.log + 1)]

    def get(self, p):  # O(1)
        return self.d[p + self.size] if 0 <= p < self.n or default is None else default

    def prod(self, l, r):  # [l, r)   O(log n)
        sml, smr = self.e, self.e
        l = max(l, 0) + self.size
        r = min(r, self.n) + self.size
        while l < r:
            if l & 1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.d[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):  # O(1)
        return self.d[1]

    def _update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def max_right(self, l, f):  # O(log n)
        if l >= self.n:
            return self.n
        l = max(l, 0) + self.size
        sm = self.e
        while True:
            while l % 2 == 0:
                l >>= 1
            if not f(self.op(sm, self.d[l])):
                while l < self.size:
                    l <<= 1
                    if f(self.op(sm, self.d[l])):
                        sm = self.op(sm, self.d[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.d[l])
            l += 1
            if l & -l == l:
                break
        return self.n

    def min_left(self, r, f):  # O(log n)
        if r <= 0:
            return 0
        r = min(r, self.n) + self.size
        sm = self.e
        while True:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not f(self.op(self.d[r], sm)):
                while r < self.size:
                    r = 2 * r + 1
                    if f(self.op(self.d[r], sm)):
                        sm = self.op(self.d[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.d[r], sm)
            if r & -r == r:
                break
        return 0

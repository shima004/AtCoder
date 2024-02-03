import itertools

n, q = map(int, input().split())
s = input()
same_char = [0] * n
for i in range(1, n):
    if s[i - 1] == s[i]:
        same_char[i] = 1

cumsum = list(itertools.accumulate(same_char))

for i in range(q):
    l, r = map(int, input().split())
    print(cumsum[r - 1] - cumsum[l - 1])

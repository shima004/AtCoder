import collections

n, q = map(int, input().split())

# set
s = collections.OrderedDict()
h = 0

for i in range(q):
    line = list(map(int, input().split()))
    if line[0] == 1:
        h += 1
        s[h] = 1
    elif line[0] == 2:
        s.pop(line[1])
    else:
        print(next(iter(s)))

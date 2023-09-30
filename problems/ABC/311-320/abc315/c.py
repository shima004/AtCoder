import collections

n = int(input())
f, s = [], []
for _ in range(n):
    s_, f_ = map(int, input().split())
    f.append(f_)
    s.append(s_)

defaultDict = collections.defaultdict(list)

for i in range(n):
    defaultDict[s[i]].append(f[i])

for i in defaultDict.keys():
    defaultDict[i].sort(reverse=True)

m = []
for i in defaultDict.keys():
    m.append(defaultDict[i][0])

m.sort(reverse=True)

if len(m) == 1:
    d_m = 0
else:
    d_m = m[0] + m[1]

for i in defaultDict.keys():
    if len(defaultDict[i]) > 1:
        d_m = max(d_m, defaultDict[i][0] + defaultDict[i][1] / 2)

print(int(d_m))

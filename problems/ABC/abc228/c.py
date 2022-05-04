n, k = map(int, input().split())
p = sorted([[sum(list(map(int, input().split()))), j]for j in range(n)], reverse=True, key=lambda x: x[0])
sub = [0]
for i in range(1, n):
  sub.append(p[i][0] - p[i-1][0])
subsub = [0]
for i in range(0, n-1):
  subsub.append(subsub[i] + sub[i+1])
print(p, sub, subsub)


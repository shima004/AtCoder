n = int(input())
r, g, b = [], [], []
for i in range(n):
  a, c = input().split()
  if c == 'R':
    r.append(a)
  elif c == 'G':
    g.append(a)
  else:
    b.append(a)
r.sort(reverse=True)
g.sort(reverse=True)
b.sort(reverse=True)

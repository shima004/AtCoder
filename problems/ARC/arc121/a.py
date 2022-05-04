from collections import defaultdict
n = int(input())
x, y = [], []
length = defaultdict(lambda: defaultdict(int))
for i in range(n):
  a, b = map(int, input().split())
  x.append([a, i])
  y.append([b, i])
x = sorted(x, reverse=True, key=lambda x:x[0])
y = sorted(y, reverse=True, key=lambda x:x[0])
if n >= 8:
  x = x[:4] + x[-4:]
  y = y[:4] + y[-4:]
for i in range(len(x)):
  for j in range(i+1, len(x), 1):
    length[x[i][1]][x[j][1]] = max(length[x[i][1]][x[j][1]], abs(x[i][0] - x[j][0]))
for i in range(len(x)):
  for j in range(i+1, len(x), 1):
    length[y[i][1]][y[j][1]] = max(length[y[i][1]][y[j][1]], abs(y[i][0] - y[j][0]))
first = [0, 0]
for i in length.items():
  for j in i[1].items():
    l = j[1]
    if first[0] < l:
      first[1] = first[0]
      first[0] = l
    elif first[1] < l:
      first[1] = l
print(first[1])
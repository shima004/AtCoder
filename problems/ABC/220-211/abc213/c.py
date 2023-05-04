height, width, n = map(int, input().split())
h, w = [], []
for i in range(n):
  a, b = map(int, input().split())
  h.append(a)
  w.append(b)
h_sort = sorted(h)
w_sort = sorted(w)
for i in range(n):
  print(h_sort.index(h[i])+1, w_sort.index(w[i])+1)

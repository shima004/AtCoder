n, k = map(int, input().split())
a = list(map(int, input().split()))
a = [[a[i], i] for i in range(n)]
a_sorted = sorted(a, key=lambda x: x[0])
a = [[i, a_sorted[i][1]] for i in range(n)]
a_sorted = sorted(a, key=lambda x: x[1])
m_all = k // n
m_th = k - (n * m_all)
for i in a_sorted:
  if i[0] <= m_th-1:
    print(m_all + 1)
  else:
    print(m_all)

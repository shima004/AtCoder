g, t, x = map(int, input().split())

for i in range(24):
  if (g >= 24):
    g = 0
  if (g == t):
    print("No")
    break
  if (g == x):
    print("Yes")
    break
  g += 1

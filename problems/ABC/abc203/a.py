a, b, c = map(int, input().split())
if (a == b):
  ans = c
elif (a == c):
  ans = b
elif (b == c):
  ans = a
else:
  ans = 0
print(ans)

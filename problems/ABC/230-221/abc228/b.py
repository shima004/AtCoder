n, x = map(int, input().split())
a = list(map(int, input().split()))
flag = [0 for i in range(n)]
ans = 0

while True:
  if (flag[x-1] == 0):
    ans += 1
    flag[x-1] = 1
    x = a[x-1]
  else:
    break

print(ans)

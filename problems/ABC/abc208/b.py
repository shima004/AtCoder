import math
p = int(input())
money = [math.factorial(i) for i in range(10, 0, -1)]
ans = 0
for i in money:
  if(p // i >= 1):
    ans += p // i
    p -= i * (p // i)
print(ans)
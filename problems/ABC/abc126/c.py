import decimal
import math
from decimal import *

n, k = map(int, input().split())
ans = Decimal("0")
for i in range(n):
  if i+1 >= k:
    ans += decimal.Decimal(1) / decimal.Decimal(n)
  else:
    ans += Decimal(str(decimal.Decimal(1) / decimal.Decimal(n))) * Decimal(str((1/2)**(1 + (math.log2(k / (i+1)) // 1))))
print(ans)
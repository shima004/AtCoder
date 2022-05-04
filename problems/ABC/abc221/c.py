import itertools

def zeroCheck(n):
  if n[0] == "0":
    return True
  if n[0] != "0":
    return False


n = str(input())
length = len(str(n))

items = list(itertools.permutations(list(n)))

ans = 0

for item in items:
  for i in range(1, length, 1):
    one = "".join(item[:i])
    two = "".join(item[i:])
    if one == "" or two == "" or zeroCheck(one) or zeroCheck(two):
      continue
    ans = max(ans, int(one) * int(two))
print(ans)


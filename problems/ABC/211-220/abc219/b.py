a = input()
b = input()
c = input()
t = input()
ans = ""
for i in t:
  if i == "1":
    ans += a
  elif i == "2":
    ans += b
  else:
    ans += c
print(ans)

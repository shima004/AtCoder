s = list(input())
t = list(input())

if s == t:
  print("Yes")
  exit()

ans = "No"

if s == t:
  ans = "Yes"

for i in range(len(s)-1):
  s[i], s[i+1] = s[i+1], s[i]

  if s == t:
    ans = "Yes"

  s[i], s[i+1] = s[i+1], s[i]

print(ans)

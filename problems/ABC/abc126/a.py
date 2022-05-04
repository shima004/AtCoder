n, k = map(int, input().split())
s = input()
ans = ""
for i, char in enumerate(s):
  if i == k - 1:
    ans += char.lower()
  else:
    ans += char
print(ans)
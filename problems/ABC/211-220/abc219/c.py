x = input()
n = int(input())
s_list = []
default = "abcdefghijklmnopqrstuvwxyz"

for i in range(n):
  s = input()
  s_new = ""
  for char in s:
    s_new += default[x.index(char)]
  s_list.append(s_new)

sorted_s = sorted(s_list)
for i in sorted_s:
  for char in i:
    print(default[x.index(char)], end="")
  print()

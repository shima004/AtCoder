n = int(input())
s = input()

ans = -1
j = 0
for i in s:
    if i == 'o':
        j += 1
    if i == '-':
        ans = max(ans, j)
        j = 0

j = 0
for i in reversed(s):
    if i == 'o':
        j += 1
    if i == '-':
        ans = max(ans, j)
        j = 0


if ans == 0:
    ans = -1
print(ans)

n = input()
s = input()


ls = s.index('|')
lf = s.rindex('|')

ans = "out"
for i in range(ls+1, lf):
    if s[i] == '*':
        ans = "in"
        break

print(ans)

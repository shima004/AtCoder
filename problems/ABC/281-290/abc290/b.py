n, k = map(int, input().split())
s = input()

ans = []
num = 0
for i in s:
    if num == k:
        ans.append('x')
    elif i == 'o':
        ans.append(i)
        num += 1
    else:
        ans.append(i)

print(''.join(ans))

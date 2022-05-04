def change(x):
    if x == '6':
        return '9'
    elif x == '9':
        return '6'
    else:
        return x

s = reversed(input())
ans = list(map(change, s))
print(''.join(ans))

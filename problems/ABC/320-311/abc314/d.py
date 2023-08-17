n = int(input())
s = input()
q = int(input())
ans = [[i, 0] for i in s]
last = [-1, 0]

for i in range(q):
    t, x, c = input().split()
    t = int(t)
    x = int(x)
    if t == 1:
        ans[x - 1] = [c, i]
    if t == 2:
        last = [0, i]
    if t == 3:
        last = [1, i]


def to_upper(c):
    if ord(c) < 97 or ord(c) > 122:
        return c
    return chr(ord(c) - 32)


def to_lower(c):
    if ord(c) < 65 or ord(c) > 90:
        return c
    return chr(ord(c) + 32)


for i in range(n):
    if ans[i][1] < last[1]:
        if last[0] == 1:
            ans[i][0] = to_upper(ans[i][0])
        else:
            ans[i][0] = to_lower(ans[i][0])

print("".join([i[0] for i in ans]))

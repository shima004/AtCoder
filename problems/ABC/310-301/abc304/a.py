n = int(input())
s = []
a = []

min_age = 10**10
min_index = 0
for i in range(n):
    _s, _a = input().split()
    s.append(_s)
    a.append(int(_a))
    if a[i] < min_age:
        min_age = a[i]
        min_index = i

ans_name = s[min_index:] + s[:min_index]
for i in range(n):
    print(ans_name[i])

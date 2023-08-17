n = int(input())
s = []
for i in range(n):
    s.append(input())

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        c = s[i] + s[j]
        if len(c) % 2 == 0:
            if c[: len(c) // 2] == c[len(c) // 2 :][::-1]:
                print("Yes")
                exit()
        else:
            if c[: len(c) // 2] == c[len(c) // 2 + 1 :][::-1]:
                print("Yes")
                exit()
print("No")

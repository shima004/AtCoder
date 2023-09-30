n = int(input())
s = input()

for i in range(1, n):
    for j in range(n):
        if i + j >= n:
            print(j)
            break
        if s[j] == s[j + i]:
            print(j)
            break

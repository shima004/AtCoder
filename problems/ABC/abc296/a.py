n = int(input())
s = input()

prev = s[0]
for i in range(1, n):
    if s[i] == prev:
        print("No")
        exit()
    prev = s[i]

print("Yes")

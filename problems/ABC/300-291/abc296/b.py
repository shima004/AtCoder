a = "abcdefgh"
for i in range(8, 0, -1):
    s = input()
    if "*" in s:
        index = s.index("*")
        print(a[index] + str(i))

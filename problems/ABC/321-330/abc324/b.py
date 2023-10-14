n = int(input())
for i in range(65):
    for j in range(65):
        if (2**i) * (3**j) == n:
            print("Yes")
            exit()
print("No")

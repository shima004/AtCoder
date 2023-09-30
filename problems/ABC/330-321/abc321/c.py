numbers = []
# bit all search
for i in range(1, 1024):
    bit = bin(i)[2:].zfill(10)
    number = ""
    for j in range(9, -1, -1):
        if bit[j] == "1":
            number += str(j)
    numbers.append(int(number))

n = int(input())
print(sorted(numbers)[n])

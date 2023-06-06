t = int(input())

for i in range(t):
    n = int(input())
    if n < 7:
        print(-1)
        continue

    n_bin = bin(n)[2:]
    if n_bin.count("1") < 3:
        while n_bin.count("1") != 3:
            n -= 1
            n_bin = bin(n)[2:]
        print(n)
    elif n_bin.count("1") == 3:
        print(int(n_bin, 2))
    else:
        count = n_bin.count("1") - 3
        n_bin = n_bin[::-1]
        while count > 0:
            n_bin = n_bin.replace("1", "0", 1)
            count -= 1
        n_bin = n_bin[::-1]
        print(int(n_bin, 2))

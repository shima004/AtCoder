n = int(input())

if n < 10**3:
    print(n)
else:
    for i in range(4, 10):
        if n < 10**i:
            n = int(n / 10 ** (i - 3)) * 10 ** (i - 3)
            print(n)
            break

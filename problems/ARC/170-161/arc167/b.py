def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


a, b = map(int, input().split())
for i in range(3):
    # print(len(make_divisors(a ** (i + 1))))
    print(len(make_divisors(a ** (i + 2))) - len(make_divisors(a ** (i + 1))))

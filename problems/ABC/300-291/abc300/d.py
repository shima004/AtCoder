n = int(input())


def get_primes(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False
    return primes


p = get_primes(int((-(-n // 12)) ** 0.5))

ans = 0
for i in range(len(p)):
    for j in range(i + 1, len(p)):
        if pow(p[i], 2) * p[j] * 25 > n:
            break
        for k in range(j + 1, len(p)):
            if pow(p[i], 2) * p[j] * pow(p[k], 2) <= n:
                ans += 1
            else:
                break
print(ans)

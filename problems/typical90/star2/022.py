from math import gcd


a, b, c = map(int, input().split())
div = gcd(a, gcd(b, c))

print((a // div) + (b // div) + (c // div) - 3)

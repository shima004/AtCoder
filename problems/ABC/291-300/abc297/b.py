a, b = map(int, input().split())
ans = 0

while a != b:
    if a == 1 or b == 1:
        ans += max(a, b) - 1
        break

    if a == 0 or b == 0:
        ans -= 1
        break

    if a > b:
        ans += a // b
        a = a % b
    else:
        ans += b // a
        b = b % a

print(ans)

a, b = map(int, input().split())
ans = 0
if a % 2 == 1 or b % 2 == 1:
    ans += 1

if (a >= 2 and a <= 3) or (b >= 2 and b <= 3):
    ans += 2

if a >= 4 or b >= 4:
    ans += 4

print(ans)

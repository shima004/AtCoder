n, k = map(int, input().split())
s = [int(input()) for _ in range(n)]
if 0 in s:
    print(n)
    exit()

left, right = 0, 0
multi = 1
ans = 0
while right < n:
    multi *= s[right]
    if multi <= k:
        right += 1
    else:
        multi //= s[left]
        left += 1
        right = max(left, right)
    ans = max(ans, right - left + 1)

print(ans)

x, y, z = map(int, input().split())
s = input()
split = []

c = s[0]
count = 0
for i in s:
    if i == c:
        count += 1
    else:
        split.append(count)
        count = 1
        c = i
split.append(count)

print(split)


def binary_search(right):
    left = 0
    while left < right:
        mid = (left + right) // 2
        if mid * y == mid * x + z:
            return mid
        elif mid * y > mid * x + z:
            right = mid
        else:
            left = mid + 1
    return left


print(binary_search(10**18))
mid = binary_search(10**18)


shift = 0
start = 0 if s[0] == "a" else 1
ans = 0
for i in split:
    if start == 0:
        if shift == 0:
            ans += x * i
        else:
            if mid > i:
                ans += y * i
            else:
                ans += (x * i) + z
                shift = 1
        start = 1
    else:
        if shift == 1:
            ans += x * i
        else:
            if mid > i:
                ans += y * i
            else:
                ans += (x * i) + z
                shift = 0
        start = 0

print(ans)

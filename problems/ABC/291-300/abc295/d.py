s = input()
rc = [0] * 1024
rc[0] = 1
c = 0
ans = 0

for i, item in enumerate(s):
    num = int(item)
    c ^= 1 << num
    rc[c] += 1

for i in rc:
    ans += i * (i - 1) // 2

print(ans)

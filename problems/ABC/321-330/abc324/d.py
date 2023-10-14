n = int(input())
s = list(input())
sorted_s = sorted(s)
max_num = 10**n

ans = 0
for i in range(10**8):
    square = str(int(i) ** 2)
    if max_num < int(square):
        break
    if sorted(square.zfill(n)) == sorted_s:
        ans += 1


print(ans)

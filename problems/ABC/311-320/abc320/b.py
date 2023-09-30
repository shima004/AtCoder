s = input()

ans = 0
for i in range(0, len(s)):
    for j in range(i + 1, len(s)):
        reverse = s[i : j + 1][::-1]
        if s[i : j + 1] == reverse:
            ans = max(ans, j - i + 1)

print(ans if ans > 0 else 1)

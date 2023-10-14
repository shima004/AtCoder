n, t = input().split()
n = int(n)
ans = []

for i in range(n):
    s = input()
    if s == t:
        ans.append(i + 1)
        continue

    if len(s) == len(t):
        count = 0
        for k in range(len(s)):
            if s[k] != t[k]:
                count += 1
        if count == 1:
            ans.append(i + 1)
            continue

    if (len(s) + 1) == len(t):
        count = 0
        j = 0
        for k in range(len(t)):
            if j == len(s):
                break
            if s[j] != t[k]:
                count += 1
                j -= 1
            j += 1
        if count <= 1:
            ans.append(i + 1)
            continue

    if (len(s) - 1) == len(t):
        count = 0
        j = 0
        for k in range(len(s)):
            if j == len(t):
                break
            if s[k] != t[j]:
                count += 1
                j -= 1
            j += 1
        if count <= 1:
            ans.append(i + 1)
            continue

print(len(ans))
print(*ans)

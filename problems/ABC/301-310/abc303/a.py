n = int(input())
s = input()
t = input()

ans = "Yes"
for i in range(n):
    if s[i] != t[i]:
        if (s[i] == "1" or t[i] == "1") and (t[i] == "l" or s[i] == "l"):
            pass
        elif (s[i] == "0" or t[i] == "0") and (t[i] == "o" or s[i] == "o"):
            pass
        else:
            ans = "No"
            break

print(ans)

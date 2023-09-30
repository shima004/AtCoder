def comp(a, b):
    bin_a = ""
    for i in range(len(a)):
        if a[i] == "?":
            bin_a += "0"
        else:
            bin_a += a[i]
    bin_b = ""
    for i in range(len(b)):
        if b[i] == "?":
            bin_b += "0"
        else:
            bin_b += b[i]

    return int(bin_a, 2) - int(bin_b, 2)


s = input()
n = int(input())

print(s)
print(bin(n))

bin_n = bin(n)[2:]
if len(bin_n) < len(s):
    bin_n = "0" * (len(s) - len(bin_n)) + bin_n

prev = False
ans = []
for i in range(len(s)):
    if s[i] == "?":
        if bin_n[i] == "0":
            if prev:
                ans.append("1")
            else:
                ans.append("0")
        elif bin_n[i] == "1":
            if i == len(s) - 1:
                ans.append("1")
                break
            if comp(s[i + 1 :], bin_n[i + 1 :]) <= 0:
                ans.append("1")
            else:
                ans.append("0")
                prev = True
    else:
        if s[i] == "0":
            if bin_n[i] == "1":
                prev = True

print(int("".join(ans), 2))

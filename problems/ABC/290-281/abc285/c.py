def convert_26(s):
    length = len(s)
    ans = 0
    for i in range(length):
        ans += (ord(s[i]) - ord('A') + 1) * 26 ** (length - i - 1)
    return ans


s = input()
print(convert_26(s))

import collections

n = int(input())
s = input()
char_map = collections.defaultdict(int)

char = s[0]
count = 1
for i in range(1, n):
    if char == s[i]:
        count += 1
    else:
        char_map[char] = max(char_map[char], count)
        char = s[i]
        count = 1

char_map[char] = max(char_map[char], count)

ans = 0
for i in char_map.values():
    ans += i

print(ans)

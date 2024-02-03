n, m = map(int, input().split())
s = list(input())
t = list(input())

n, m = 2 * 10**5, 1
s = ["a" for _ in range(n)]
t = ["a" for _ in range(m)]


def is_replacable(s, t):
    for i in range(len(s)):
        if s[i] != t[i] and s[i] != "#":
            return False
    return True


for j in range(n - m + 1):
    if is_replacable(s[j : j + m], t):
        s[j : j + m] = ["#" for _ in range(m)]


for j in range(n - m + 1):
    if is_replacable(s[j : j + m], t):
        s[j : j + m] = ["#" for _ in range(m)]

import queue

n = int(input())
s = input()

ans = list(s)

i = 0
c = queue.LifoQueue()
while True:
    if i == n:
        break
    if s[i] == "(":
        c.put(i)
    elif s[i] == ")":
        if c != []:
            _c = c.get()
            ans[_c : i + 1] = ":" * (i - _c + 1)
    i += 1

print("".join(ans).replace(":", ""))

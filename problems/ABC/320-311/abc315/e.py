n = int(input())
p = []

for _ in range(n):
    p.append(list(map(int, input().split()))[1:])

ready = [False] * n
stack = p[0]
ans = []
while stack:
    i = stack.pop()
    if ready[i - 1]:
        continue
    readable = True
    for j in p[i - 1]:
        if not ready[j - 1]:
            readable = False
            break
    if not readable:
        stack.append(i)
        stack.extend(p[i - 1])
        continue
    ready[i - 1] = True
    ans.append(i)

print(*ans, sep=" ")

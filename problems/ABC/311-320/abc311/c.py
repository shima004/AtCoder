n = int(input())
path = list(map(int, input().split()))
path = [i - 1 for i in path]
sarched = [False] * n


for i in range(n):
    p = [i]
    next = path[i]
    if sarched[i]:
        continue
    sarched[i] = True
    for j in range(n):
        p.append(next)
        next = path[next]
        if next == i:
            print(len(p))
            p = [i + 1 for i in p]
            print(*p)
            exit()

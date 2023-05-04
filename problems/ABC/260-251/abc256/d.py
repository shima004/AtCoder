N = int(input())
path = [list(map(int, input().split())) for i in range(N)]
path.sort(key=lambda x: x[0])
merged = [path[0]]
for w in path:
    if w[0] > merged[-1][1]:
        merged.append(w)
    elif w[1] > merged[-1][1]:
        merged[-1][1] = w[1]

for w in merged:
    print(w[0], w[1])

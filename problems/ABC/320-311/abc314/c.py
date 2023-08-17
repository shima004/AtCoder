from collections import defaultdict

n, m = map(int, input().split())
s = input()
c = list(map(int, input().split()))
ans = [0] * (n)

df = defaultdict(list)

for i in range(n):
    df[c[i]].append(i)

for i in range(m):
    move = df[i + 1]
    for j in range(len(move) - 1):
        ans[move[j + 1]] = s[move[j]]
    ans[move[0]] = s[move[-1]]

print("".join(ans))

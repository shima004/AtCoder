n, k = map(int, input().split())
rank = []

for i in range(n):
    s = input()
    if i <= k-1:
        rank.append(s)

rank = sorted(rank)
for i in rank:
    print(i)

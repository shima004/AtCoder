n, m = map(int, input().split())
a = list(map(int, input().split()))
l = [i+1 for i in range(n)]
l = list(reversed(l))
stock = []
ans = []

while len(l) >= 1:
    c = l.pop()
    if c in a:
        stock.append(c)
    else:
        ans.append(c)
        while len(stock) >= 1:
            ans.append(stock.pop())
        stock = []

while len(stock) >= 1:
    ans.append(stock.pop())

for i in ans:
    print(i, end=" ")
print()

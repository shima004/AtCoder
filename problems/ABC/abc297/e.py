import heapq

n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
q = [0]
ans = []
for i in range(k):
    x = heapq.heappop(q)
    for j in a:
        y = x + j
        if y not in ans:
            ans.append(y)
            heapq.heappush(q, y)

print(heapq.heappop(q))

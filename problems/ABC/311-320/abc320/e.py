import heapq

n, m = map(int, input().split())

ans = [0 for i in range(n)]
limit = []
humans = [i for i in range(n)]
for i in range(m):
    t, w, s = map(int, input().split())
    while limit and limit[0][0] <= t:
        _, h = heapq.heappop(limit)
        heapq.heappush(humans, h)

    if not humans:
        continue
    h = heapq.heappop(humans)
    ans[h] += w
    heapq.heappush(limit, (s + t, h))

print(*ans, sep="\n")

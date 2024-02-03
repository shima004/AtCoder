n, q = map(int, input().split())
c = list(map(int, input().split()))
boxes = [set() for _ in range(n)]
for i in range(n):
    boxes[i].add(c[i])

for i in range(q):
    f, t = map(int, input().split())
    f -= 1
    t -= 1
    if len(boxes[f]) < len(boxes[t]):
        boxes[t] |= boxes[f]
        boxes[f] = set()
    else:
        boxes[f] |= boxes[t]
        boxes[t] = set()
        boxes[f], boxes[t] = boxes[t], boxes[f]

    print(len(boxes[t]))

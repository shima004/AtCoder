n = int(input())
q = int(input())
query2 = [[] for i in range(n + 1)]
query3 = [[] for i in range(2 * 10**5 + 1)]

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        i, j = query[1:]
        query2[j].append(i)
        query3[i].append(j)
    elif query[0] == 2:
        i = query[1]
        for i in sorted(query2[i]):
            print(i, end=" ")
        print()
    else:
        i = query[1]
        b = -1
        for i in sorted(query3[i]):
            if b != i:
                print(i, end=" ")
                b = i
        print()

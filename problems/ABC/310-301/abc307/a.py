n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    print(sum(a[i * 7 : (i + 1) * 7]), end=" ")
print()

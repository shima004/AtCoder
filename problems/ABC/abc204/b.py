n = int(input())
a = list(map(lambda x: int(x) - 10 if int(x) > 10 else 0, input().split()))
print(sum(a))
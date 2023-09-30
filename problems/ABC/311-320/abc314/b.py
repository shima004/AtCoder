n = int(input())
targets = []
for i in range(n):
    c = int(input())
    target = list(map(int, input().split()))
    targets.append(target)
x = int(input())
indexes = []
min_len = 10000000
for i in range(n):
    if x in targets[i]:
        if len(targets[i]) < min_len:
            min_len = len(targets[i])
            indexes = [i + 1]
        elif len(targets[i]) == min_len:
            indexes.append(i + 1)

sorted_indexes = sorted(indexes)
print(len(sorted_indexes))
print(" ".join(map(str, sorted_indexes)))

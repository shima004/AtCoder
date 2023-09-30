import collections

m = int(input())
s1 = input()
s2 = input()
s3 = input()

set1 = set(s1)
set2 = set(s2)
set3 = set(s3)

all_set = set1 & set2 & set3
if len(all_set) == 0:
    print(-1)
    exit()

s1 = s1 * 3
s2 = s2 * 3
s3 = s3 * 3
ans = 1000
for i in range(len(s1)):
    for j in range(len(s1)):
        for k in range(len(s1)):
            if i == j or j == k or k == i:
                continue
            if s1[i] == s2[j] == s3[k]:
                ans = min(ans, max(i, j, k))

print(ans)

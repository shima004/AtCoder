N, Q = map(int, input().split())
ans = [i + 1 for i in range(N)]
index_map = [i for i in range(N)]

for i in range(Q):
    num = int(input())
    index = index_map[num - 1]

    if index == N - 1:
        left_num = ans[index - 1]
        index_map[num - 1] = index - 1
        index_map[left_num - 1] = index
        ans[index] = left_num
        ans[index - 1] = num
    else:
        right_num = ans[index + 1]
        index_map[num - 1] = index + 1
        index_map[right_num - 1] = index
        ans[index] = right_num
        ans[index + 1] = num

for i in ans:
    print(i, end=" ")
print()

from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))
sorted_a = sorted(a)
sorted_a = deque(sorted_a)

if len(sorted_a) % 2 == 1:
    head = sorted_a[1] - sorted_a[0]
    tail = sorted_a[-1] - sorted_a[-2]
    left_middle = sorted_a[len(sorted_a) // 2] - sorted_a[len(sorted_a) // 2 - 1]
    right_middle = sorted_a[len(sorted_a) // 2 + 1] - sorted_a[len(sorted_a) // 2]
    # 最も大きいものを取り除く
    if head < tail and head < left_middle and head < right_middle:
        sorted_a.popleft()
    elif tail < head and tail < left_middle and tail < right_middle:
        sorted_a.pop()
    elif left_middle < head and left_middle < tail and left_middle < right_middle:
        sorted_a.pop()
        sorted_a.popleft()
    else:
        sorted_a.pop()
        sorted_a.popleft()

ans = 0
for i in range(k // 2):
    head = sorted_a[1] - sorted_a[0]
    tail = sorted_a[-1] - sorted_a[-2]
    if head < tail:
        ans += head
        sorted_a.popleft()
        sorted_a.popleft()
    else:
        ans += tail
        sorted_a.pop()
        sorted_a.pop()

print(ans)

n, x = map(int, input().split())
a = list(map(int, input().split()))
sorted_a = sorted(a)


def binary_search(target, sorted_list):
    left = 0
    right = len(sorted_list)
    while left < right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] > target:
            right = mid
        else:
            left = mid + 1
    return -1


for i in range(n):
    a_i = a[i]
    target = -(x - a_i)
    if binary_search(target, sorted_a) != -1:
        print("Yes")
        exit()

print("No")

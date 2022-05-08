def binary_search(a, x, boolfunc):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if boolfunc(a[mid], x):
            right = mid - 1
        else:
            left = mid + 1
    return left

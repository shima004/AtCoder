n = int(input())
w = input().split()

english = ["and", "not", "that", "the", "you"]

ans = "No"
for i in w:
    if i in english:
        ans = "Yes"

print(ans)

n = int(input())

users = dict()
for i in range(n):
    user = input()
    if user in users:
        continue
    else:
        users[user] = 1
        print(i + 1)

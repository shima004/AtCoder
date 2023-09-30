n = input()
number = list(map(int, n))
sorted_number = sorted(number, reverse=True)
same = True
for i in range(len(number)):
    if number[i] != sorted_number[i]:
        same = False
        break

if len(set(number)) != len(number):
    same = False

if same:
    print("Yes")
else:
    print("No")

n = input()

prev = 0
for i in range(20):
    print("? " + str(i+2))
    s = int(input())
    if s != prev:
        print("! " + str(i+1))
        exit()
    prev = s

print("! " + str(21))

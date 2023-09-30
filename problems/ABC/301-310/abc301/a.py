n = int(input())
s = input()
t = s.count("T")
a = s.count("A")

if t == a:
    if s.rindex("T") > s.rindex("A"):
        print("A")
    else:
        print("T")
elif a < t:
    print("T")
else:
    print("A")

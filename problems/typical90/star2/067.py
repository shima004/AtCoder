from numpy import base_repr

n, k = input().split()
for i in range(int(k)):
    n = int(n, 8)
    n = base_repr(n, 9)
    n = n.replace('8', '5')
print(n)

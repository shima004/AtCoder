H, W = map(int, input().split())
R, C = map(int, input().split())
if H == 1 and W == 1:
    print(0)
elif H == 1:
    if C == 1 or C == W:
        print(1)
    else:
        print(2)
elif W == 1:
    if R == 1 or R == H:
        print(1)
    else:
        print(2)

elif H == R and W == C or R == 1 and C == 1 or R == 1 and W == C or H == R and C == 1:
    print(2)
elif H == R or W == C or R == 1 or C == 1:
    print(3)
else:
    print(4)

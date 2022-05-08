from cmath import cos, sin, sqrt

from numpy import arctan2, deg2rad, rad2deg


T = int(input())
L, X, Y = map(int, input().split())
R = L / 2
Q = int(input())
for i in range(Q):
    t = int(input())
    y, z = R * sin(deg2rad(360 * t/T)), R * cos(deg2rad(360 * t/T))
    a = sqrt(X ** 2 + (Y - y) ** 2)
    print(a, z)
    print(rad2deg(arctan2(a.real, z.real)))

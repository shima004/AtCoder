from cmath import cos, sin, sqrt

from numpy import arctan2, deg2rad, rad2deg

T = int(input())
L, X, Y = map(int, input().split())
R = L / 2
Q = int(input())
for i in range(Q):
    t = int(input())
    x = X
    y = Y + R * sin(deg2rad(360 * t / T))
    z = R - R * cos(deg2rad(360 * t / T))
    print(rad2deg(arctan2(z.real, sqrt(x**2 + y**2).real)))

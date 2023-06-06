import math
import sys

sys.setrecursionlimit(10**6)

n, d = map(int, input().split())
places = []
for i in range(n):
    x, y = map(int, input().split())
    places.append([x, y, 0])


def bfs(place, places):
    for i in range(n):
        if places[i][2] == 1:
            continue
        if (
            math.sqrt((place[0] - places[i][0]) ** 2 + (place[1] - places[i][1]) ** 2)
            <= d
        ):
            places[i][2] = 1
            bfs(places[i], places)


places[0][2] = 1
bfs(places[0], places)


for i in range(n):
    if places[i][2] == 1:
        print("Yes")
    else:
        print("No")

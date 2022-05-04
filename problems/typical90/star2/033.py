from math import ceil

h, w = map(int, input().split())

lights = ceil(h / 2) * ceil(w / 2) if h != 1 and w != 1 else h * w

print(lights)

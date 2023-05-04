import collections
from sys import stdin

numbers = [[0 for _ in range(10)] for _ in range(10)]

N = int(input())
S = [stdin.readline().strip() for _ in range(N)]

for reel in S:
    for i, c in enumerate(reel):
        numbers[int(c)][i] += 1

time = 0
for i in range(N):
    for j in range(10):
        for k in range(10):
            if numbers[k][j] > 0:
                numbers[k][j] -= 1
        time += 1
        for k in range(10):
            if sum(numbers[k]) == 0:
                print(time-1)
                exit()

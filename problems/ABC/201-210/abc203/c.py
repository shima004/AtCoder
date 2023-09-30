n, place = map(int, input().split())
friends = sorted([list(map(int, input().split())) for i in range(n)], key=lambda x: x[0])
for friend in friends:
  if friend[0] <= place:
    place += friend[1]
  else:
    break

print(place)

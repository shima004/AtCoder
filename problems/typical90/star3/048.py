N, K = map(int, input().split())
point = [list(map(int, input().split())) for i in range(N)]
score = [i[1] for i in point]
score.extend([i[0] - i[1] for i in point])
score.sort(reverse=True)
print(sum(score[:K]))

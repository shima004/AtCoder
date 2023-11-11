import sys


def dijkstra(graph, start):
    n = len(graph)
    visited = [False] * n
    distance = [sys.maxsize] * n
    distance[start] = 0

    for _ in range(n):
        min_distance = sys.maxsize
        for j in range(n):
            if not visited[j] and distance[j] < min_distance:
                min_distance = distance[j]
                u = j
        visited[u] = True
        for v in range(n):
            if not visited[v] and graph[u][v] != 0:
                new_distance = distance[u] + graph[u][v]
                if new_distance < distance[v]:
                    distance[v] = new_distance

    return distance


def keep_nodes(graph, nodes):
    """
    二次元配列graphから、指定されたノード以外を削除した二次元配列を返す
    """
    n = len(graph)
    new_graph = [[0] * n for _ in range(n)]
    for i in range(n):
        if i not in nodes:
            continue
        for j in range(n):
            if j not in nodes:
                continue
            new_graph[i][j] = graph[i][j]
    return new_graph


n, a, b, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
car = [[i * a for i in graph[j]] for j in range(n)]
train = [[(i * b) + c for i in graph[j]] for j in range(n)]
train_distance = dijkstra(train, 0)

car_distance = dijkstra(car, 0)
car_distance = [[car_distance[i], i] for i in range(n)]
sorted_car_distance = sorted(car_distance, key=lambda x: x[0])
print(sorted_car_distance)

dp = [[0, 0] for _ in range(n)]
ans = 10**18

for i in range(n):
    sum_distance = sorted_car_distance[i][0]
    remain_path = []
    for j in car_distance[i:]:
        remain_path.append(j[1])
    remain_path = keep_nodes(train, remain_path)
    point = sorted_car_distance[i][1]
    train_distance = dijkstra(remain_path, point)
    _max = 0
    for j in train_distance:
        if j > _max and j != sys.maxsize:
            _max = j
    print(_max, sum_distance, point)
    print(remain_path)
    print(train_distance)

    if sum_distance + _max < ans:
        ans = sum_distance + _max

print(ans)

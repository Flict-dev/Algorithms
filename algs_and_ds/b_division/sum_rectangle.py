n, m, k = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]
cords = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]

for x1, y1, x2, y2 in cords:
    print(sum(data[x1][x1 : y2 + 1]) + sum(data[x2][x1 : y2 + 1]))

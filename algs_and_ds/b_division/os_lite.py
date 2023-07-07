l = int(input())
n = int(input())

data = []
for _ in range(n):
    a, b = map(int, input().split())
    new = list(filter(lambda i: not (i[0] <= b and a <= i[1]), data))
    data = new + [(a, b)]
print(len(data))

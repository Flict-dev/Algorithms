n = int(input())
data = [int(input()) for _ in range(n)]

res = 0
for i in range(len(data) - 1):
    if data[i] == data[i + 1]:
        res += data[i]
    elif data[i] > data[i + 1]:
        res += data[i + 1]
    else:
        res += data[i]
print(res)

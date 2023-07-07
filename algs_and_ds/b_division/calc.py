# 3 4 6 12 13 14
# res = 0
# data = list(sorted([3, 13, 12, 4, 14, 6]))
# res = data[1] - data[0] + data[-1] - data[-2]
# print(res)


def max_length(i):
    if i > n - 3:
        return 0
    if m[i] == 0:
        m[i] = x[i + 1] - x[i] + max(max_length(i + 2), max_length(i + 3))
    return m[i]


n = int(input())
x = list(sorted(map(int, input().split())))

m = [0 for _ in range(n)]
print(x[-1] - x[0] - max(max_length(1), max_length(2)))

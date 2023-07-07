n, k, r, l = map(int, [input() for _ in range(4)])

var1 = (r - 1) * 2 + l + k
var2 = (r - 1) * 2 + l - k


if var1 > n and var2 < 1:
    print(-1)
else:
    bob = var1 if var1 <= n else var2
    x = (bob - l) // 2 + 1
    print(x, 2 - bob % 2)

"""
Попробовать вариант с масивом и поиском через index со срезом в (r - 1) * 2 + l
"""

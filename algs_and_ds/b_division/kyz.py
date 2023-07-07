n, k = map(int, input().split())
a = [1]
for i in range(1, n + 1):
    r = k
    if i < r:
        r = i
    a.append(0)
    for j in range(1, r + 1):
        a[i] = a[i] + a[i - j]
print(a[n - 1])

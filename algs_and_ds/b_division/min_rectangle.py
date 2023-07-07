n = int(input())
x, y = [], []
for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
print(f"{min(x)} {min(y)} {max(x)} {max(y)}")

q = int(input())

train_cars = list(map(int, input().split()))
res = []
stack = []
for i in range(q):
    if not len(stack):
        stack.append(train_cars[i])
    elif stack[-1] >= train_cars[i]:
        stack.append(train_cars[i])
    elif stack[-1] < train_cars[i]:
        while len(stack) and stack[-1] <= train_cars[i]:
            res.append(stack.pop())
        stack.append(train_cars[i])

print("YES" if sorted(train_cars) == res + stack[::-1] else "NO")

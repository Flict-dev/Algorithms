n = int(input())
data = list(map(int, input().split()))

stack = []
res = []

for i in range(len(data)):
    if not len(stack):
        stack.append((i, data[i], -1))
    elif stack[-1][1] <= data[i]:
        stack.append((i, data[i], -1))
    elif stack[-1][1] > data[i]:
        while len(stack) > 0 and stack[-1][1] > data[i]:
            res.append((*stack.pop()[0:2], i))
        stack.append((i, data[i], -1))

out = sorted(res + stack, key=lambda x: x[0])

print(" ".join(map(lambda x: str(x[2]), out)))

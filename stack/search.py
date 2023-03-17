"""
Поиск ближайшего меньшего справа
"""

data = [7, 2, 4, 5, 3, 2, 5, 1, 5, 4]
res = []
stack = []

for i in range(len(data)):
    if len(stack) < 1:
        stack.append((i, data[i]))

    elif stack[-1][1] > data[i]:
        while stack and stack[-1][1] > data[i]:
            cur = stack.pop()
            res.append((*cur, i))
        stack.append((i, data[i]))

    elif stack[-1][1] < data[i]:
        stack.append((i, data[i]))

for i in range(len(stack)):
    res.append((*stack[i], len(data)))

print(sorted(res))

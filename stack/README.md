# Тренировки по алгоритмам 3.0. [Лекция 1: «Стеки»](https://www.youtube.com/live/ZUpImO_2hmA?feature=share)

## 1. Инфиксная запись выражения в постфиксную при помощи стека
![image](https://user-images.githubusercontent.com/76905733/225863626-611f96f3-cfc7-479e-815c-92ebfaa8f581.png)
`Решение`
```python
# Операции с значениями их приоритетов
operations = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
}


def infix_to_postfix(row: str):
    res, stack = "", []

    for i in row:
        if i.isdigit():
            res += i

        elif not len(stack) or i == "(" or stack[-1] == "(":
            stack.append(i)

        elif i == ")":
            for j in range(len(stack) - 1, 0, -1):
                if stack[j] != "(":
                    res += stack.pop()
                else:
                    stack.pop()
                    break

        elif operations[i] <= operations[stack[-1]]:
            while operations[i] <= operations[stack[-1]]:
                res += stack.pop()
            stack.append(i)

        else:
            stack.append(i)

    return res + "".join(stack)


print("6+3*(1+4*5)*2")
print(infix_to_postfix("6+3*(1+4*5)*2"))

# 6+3*(1+4*5)*2
# 63145*+*2+*
```
---

## 2. Поиск ближайшего меньшего справа
![image](https://user-images.githubusercontent.com/76905733/225865084-a3c49e34-0aa0-44c9-89f9-1ac0da66eaea.png)
![image](https://user-images.githubusercontent.com/76905733/225865261-467f89f0-a6fa-435c-8298-ec9c8b72a80f.png)


`Решение`
Добавляем в стек числа, пока они меньше добавляемых. Если число больше, то устанавливаем текущее как минимум
```python
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
```
---
## 3.Реализация рекурсивной функции при помощи стэка без рекурсии
```python
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

stack = [{"n": 4, "prev": "?", "labelfrom": 0}]
while len(stack) > 0:

    localvars = stack[-1]
    labelfrom = localvars["labelfrom"]
    
    """Labelfrom 0 означает обработку входа в функцию"""
    if labelfrom <= 0:
        print(stack)
        if localvars["n"] == 1:
            returnedvalue = 1
            stack.pop()
            continue
        localvars["labelfrom"] = 1
        stack.append({"n": localvars["n"] - 1, "prev": "?", "labelfrom": 0})
        continue
    
    """Labelfrom 1 означает обработку выхода из функции"""
    if labelfrom <= 1:
        localvars["prev"] = returnedvalue
        returnedvalue = localvars["prev"] * localvars["n"]
        print(stack)
        stack.pop()

print(returnedvalue)
```

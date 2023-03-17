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

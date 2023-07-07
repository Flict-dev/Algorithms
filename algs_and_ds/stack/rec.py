def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


"""Реализация рекурсивной функции при помощи стэка без рекурсии)"""

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
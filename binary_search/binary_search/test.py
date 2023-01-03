def f(x, a):
    return (x % 12 == 0) and (x in list(range(70, 81))) and (not (x % a == 0))


for a in range(1, 100):
    for x in range(1, 10000):
        if not f(x, a):
            break
    else:
        print(a, x)
        break

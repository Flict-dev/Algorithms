from collections import deque

first = deque(map(int, input().split()))
second = deque(map(int, input().split()))

c = 0
while first and second:
    f_v = first.popleft()
    s_v = second.popleft()
    if s_v > f_v and (f_v, s_v) != (0, 9) or (s_v, f_v) == (0, 9):
        second.append(f_v)
        second.append(s_v)
    else:
        first.append(f_v)
        first.append(s_v)

    c += 1
    if c >= 10**6:
        print("botva")
        exit()

winner = "first" if first else "second"
print(f"{winner} {c}")

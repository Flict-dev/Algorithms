class Deque:
    def __init__(self) -> None:
        self.__deque = []

    @property
    def size(self):
        return len(self.__deque)

    def push_back(self, value: int):
        self.__deque.append(value)
        return "ok"

    def push_front(self, value: int):
        self.__deque = [value] + self.__deque
        return "ok"

    def pop_back(self):
        if len(self.__deque):
            return self.__deque.pop()
        return "error"

    def pop_front(self):
        if len(self.__deque):
            copy = self.__deque[0]
            del self.__deque[0]
            return copy
        return "error"

    @property
    def front(self):
        if len(self.__deque):
            return self.__deque[0]
        return "error"

    @property
    def back(self):
        if len(self.__deque):
            return self.__deque[-1]
        return "error"

    def clear(self):
        self.__deque.clear()
        return "ok"


def parse_command(command: str):
    data = command.split()
    if len(data) > 1:
        return (data[0], int(data[1]))
    return (data[0], None)


d = Deque()
commands = {
    "push_back": lambda x: d.push_back(x),
    "push_front": lambda x: d.push_front(x),
    "size": lambda: d.size,
    "back": lambda: d.back,
    "front": lambda: d.front,
    "pop_back": lambda: d.pop_back(),
    "pop_front": lambda: d.pop_front(),
    "clear": lambda: d.clear(),
}


command = input()
while command != "exit":
    com, val = parse_command(command)
    if val is None:
        print(commands[com]())
    else:
        print(commands[com](val))
    command = input()
print("bye")
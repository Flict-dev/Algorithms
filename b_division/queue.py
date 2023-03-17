class Queue:
    def __init__(self) -> None:
        self.__queue = []

    @property
    def size(self):
        return len(self.__queue)

    def push(self, value: int):
        self.__queue.append(value)
        return "ok"

    def pop(self):
        if len(self.__queue):
            copy = self.__queue[0]
            del self.__queue[0]
            return copy
        return "error"

    @property
    def front(self):
        if len(self.__queue):
            return self.__queue[0]
        return "error"

    def clear(self):
        self.__queue.clear()
        return "ok"


def parse_command(command: str):
    data = command.split()
    if len(data) > 1:
        return (data[0], int(data[1]))
    return (data[0], None)


q = Queue()
commands = {
    "push": lambda x: q.push(x),
    "size": lambda: q.size,
    "front": lambda: q.front,
    "pop": lambda: q.pop(),
    "clear": lambda: q.clear(),
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

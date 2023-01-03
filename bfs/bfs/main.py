# from collections import deque


class Queue:
    def __init__(self, array: list) -> None:
        self.list = array

    def __str__(self) -> str:
        return f"{self.list}"

    def append(self, values: list):
        for val in values:
            if val not in self.list:
                self.list.append(val)

    def popleft(self):
        try:
            val = self.list[0]
            del self.list[0]
            return val
        except IndexError:
            return None


def bfs(graph, func):
    heap = Queue(graph[list(graph.keys())[0]])
    while heap:
        guess = heap.popleft()
        if func(guess):
            return guess
        else:
            heap.append(graph[guess])
    return None


def check_function(item: str):
    return item[-1] == "m"


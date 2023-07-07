"""
heap:

parent = (i - 1) // 2

child 1 = 2*i + 1
child 2 = 2*i + 2


0 1 2  3 4 5  6  7  8 
2 5 4 11 6 8 25 12 20
"""


class Heap:
    def __init__(self) -> None:
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        pos = len(self.heap) - 1
        while pos > 0 and self.heap[pos] > self.heap[(pos - 1) // 2]:
            self.heap[pos], self.heap[(pos - 1) // 2] = (
                self.heap[(pos - 1) // 2],
                self.heap[pos],
            )
            pos = (pos - 1) // 2

    def extract(self):
        ans, pos = self.heap[0], 0
        self.heap[0] = self.heap[-1]

        while pos * 2 + 2 < len(self.heap):
            child = pos * 2 + 1
            if self.heap[child] < self.heap[child + 1]:
                child += 1
            if self.heap[child] > self.heap[pos]:
                self.heap[pos], self.heap[child] = self.heap[child], self.heap[pos]
                pos = child
            else:
                break
        self.heap.pop()
        return ans


h = Heap()
n = int(input())
for _ in range(n):
    com = list(map(int, input().split()))
    if not com[0]:
        h.insert(com[1])
    else:
        print(h.extract())

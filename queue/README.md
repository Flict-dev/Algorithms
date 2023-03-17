# Очередь

### First in frist out реализация кольцевого буфера для очереди
```python
class Circle:
    """k - максимальное кол-во элементов в круге"""

    def __init__(self, k: int) -> None:
        self.k = k
        self.head = 0
        self.tail = 0
        self.circle = [0 for _ in range(k)]

    def __str__(self) -> str:
        return f"{self.circle=}\n {self.head=} {self.tail=}"

    def append(self, value):
        self.circle[self.tail % self.k] = value
        self.tail += 1
        self.head = self.tail % self.k

    def pop(self):
        if self.head >= self.tail:
            return "Circle is empty"
        res = self.circle[self.head % self.k]
        self.circle[self.head % self.k] = 0
        self.head += 1
        return res
# Пример
round = Circle(5)
for i in range(1, 100):
    round.append(i)
print(round)

```

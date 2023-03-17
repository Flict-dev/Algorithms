# Тренировки по алгоритмам 3.0. [Лекция 2: «Очереди, деки и приоритетные очереди»](https://www.youtube.com/live/sAyOhkMZae4?feature=share)

## Куча (бинарное дерево максимума или минимума)
![image](https://user-images.githubusercontent.com/76905733/225870893-7f498daa-8778-4985-9e28-fdb419b811dd.png)
```
Родитель - (i - 1) // 2

Ребенок1 - 2*i + 1
Ребенок2 - 2*i + 2
```
`Реализация кучи максимума`
```python
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
```

---
## Пирамидальная сортировка
`Алгоритм`
```
1. Получаем текущий максимум в куче
2. Добавляем его в конец списка
3. Уменьшаем размер кучи и просеиваем кучу вниз
Повтор пока длина кучи не равна 1
```
```python
# Функция просеивания кучи вниз 
def heapify(heap: list, len_heap: int):
    if len_heap == 2 and heap[0] < heap[1]:
        heap[0], heap[1] = heap[1], heap[0]
        return heap
    parrent = (len_heap - 2) // 2

    for pos in range(parrent, -1, -1):
        while 2 * pos + 2 <= len_heap:
            max_child = 2 * pos + 1

            if 2 * pos + 2 != len_heap and heap[max_child] < heap[max_child + 1]:
                max_child += 1
            if heap[max_child] > heap[pos]:
                heap[pos], heap[max_child] = heap[max_child], heap[pos]
                pos = max_child
            else:
                break
    return heap


def heapy_sort(heap: list, len_heap: int):
    for len_heap in range(len_heap - 1, 0, -1):
        heap[0], heap[len_heap] = heap[len_heap], heap[0]
        pos = 0
        while 2 * pos + 2 < len_heap:
            child = 2 * pos + 1
            if heap[child] < heap[child + 1]:
                child += 1
            if heap[pos] < heap[child]:
                heap[pos], heap[child] = heap[child], heap[pos]
                pos = child
            else:
                break
    if heap[0] > heap[1]:
        heap[0], heap[1] = heap[1], heap[0]
    return heap


n = int(input())
data = list(map(int, input().split()))

if n <= 1:
    print(*data)
    exit()

heap = heapify(data, n)
print(*heapy_sort(heap, n))

```

# Бинарный поиск

## Реализация бинарного поиска
```python
def binary_search(data: list, num: int):
    sorted_data = sorted(data)
    high, low, = (
        len(sorted_data) - 1,
        0,
    )
    while low <= high:
        mid = (low + high) // 2
        guess = sorted_data[mid]
        if guess == num:
            return mid
        elif num > guess:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

## Реализация тернарного поиска
Хз зачем, но вот
```python
def ternary_search(item, array):
    l, r = 0, len(array) - 1
    while l <= r:
        h = (r - l) // 3
        m1 = l + h
        m2 = r - h
        if item == array[m1]:
            return m1
        if item == array[m2]:
            return m2
        if array[m1] < item < array[m2]:
            l = m1 + 1
            r = m2 - 1
        elif item < array[m1]:
            r = m1 - 1
        else:
            l = m2 + 1
    return -1
```

heap = []

"""
heap:

parent = (i - 1) // 2

child 1 = 2*i + 1
child 2 = 2*i + 2


0 1 2  3 4 5  6  7  8 
2 5 4 11 6 8 25 12 20
"""


def push_heap(value: int, heap: list):
    heap.append(value)
    pos = len(heap) - 1
    while pos != 0 and heap[pos] < heap[(pos - 1) // 2]:
        heap[pos], heap[(pos - 1) // 2] = heap[(pos - 1) // 2], heap[pos]
        pos = (pos - 1) // 2
    return heap


def pop_heap(heap: list):
    ans, heap[0] = heap[0], heap[-1]
    pos = 0
    while pos * 2 + 1 < len(heap) - 1:
        min_child = pos * 2 + 1
        if heap[min_child] > heap[min_child + 1]:
            min_child += 1
        if heap[min_child] < heap[pos]:
            heap[pos], heap[min_child] = heap[min_child], heap[pos]
            pos = min_child
        else:
            break
    heap.pop()
    print(heap)
    return ans


print(push_heap(3, [2, 5, 4, 11, 6, 8, 25, 12, 20]))
print(pop_heap([2, 5, 4, 11, 6, 8, 25, 12, 20]))

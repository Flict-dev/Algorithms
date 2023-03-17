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

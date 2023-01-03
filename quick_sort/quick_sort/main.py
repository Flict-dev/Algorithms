def rec_sum(array: list):
    """
    Implementation of the sum based on the principle of divide and conquer
    """
    if len(array) == 0:
        return 0
    return array.pop() + rec_sum(array)


def quicksort(array: list):
    """
    Implementation of the quick sort alg based on the principle of divide and conquer
    """
    if len(array) < 2:
        return array

    pivot = array[0]

    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)

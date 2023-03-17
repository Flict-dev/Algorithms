from quick_sort.main import quicksort, rec_sum


def test_quicksort():
    assert quicksort([6, 1, 5, 86, 41, 63, 956, 3, 5, 4, 7]) == sorted(
        [6, 1, 5, 86, 41, 63, 956, 3, 5, 4, 7]
    )


def test_sum():
    assert rec_sum([i for i in range(20)]) == sum([i for i in range(20)])
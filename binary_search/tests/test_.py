from binary_search.main import binary_search


def test_bin_search():
    assert binary_search([i for i in range(10000)], 9998) != -1

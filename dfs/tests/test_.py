from dfs.main import dfs


def test_dfs():
    graph1 = {"A": {"B": 6, "C": 2}, "B": {"D": 1}, "C": {"B": 3, "D": 5}, "D": {}}
    graph2 = {
        "A": {"B": 10},
        "B": {"D": 20},
        "C": {"B": 1},
        "D": {"C": 1, "E": 30},
        "E": {},
    }
    graph3 = {
        "A": {"B": 5, "C": 2},
        "B": {"D": 4, "E": 2},
        "C": {"B": 8, "E": 7},
        "D": {"F": 3, "E": 6},
        "E": {"F": 1},
        "F": {},
    }

    assert dfs(graph1, "A", "D") == ("ACBD", 6)
    assert dfs(graph2, "A", "E") == ("ABDE", 60)
    assert dfs(graph3, "A", "F") == ("ABEF", 8)

from bfs.main import bfs, check_function


def test_bfs():
    g = {
        "you": ["alice", "bob", "claire"],
        "peggy": ["jhom"],
        "bob": ["anuj", "peggy"],
        "alice": ["peggy"],
        "claire": ["thom", "jhony"],
        "jhony": [],
        "thom": [],
        "anuj": [],
    }

    assert bfs(g, check_function) == "thom"

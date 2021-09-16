def increase_one(x):
    return x + 1


def decrease_one(x):
    return x - 1


def test_increase_one():
    assert increase_one(4) == 5
    assert decrease_one(5) == 4

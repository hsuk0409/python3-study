import pytest


@pytest.fixture()
def get_random_number():
    import random
    return random.randrange(0, 10)


def test_get_random_number(get_random_number):
    assert 0 < get_random_number < 10

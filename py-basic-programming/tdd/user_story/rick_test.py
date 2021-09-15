import unittest


class Rick(object):
    def __init__(self, universe):
        self.universe = universe


class RickTests(unittest.TestCase):
    def test_universe(self):
        rick = Rick(111)
        self.assertEqual(rick.universe, 111)


if __name__ == '__main__':
    unittest.main()

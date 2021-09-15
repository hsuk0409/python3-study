import unittest


class Citadel(object):
    def __init__(self):
        self.residents = []

    def get_add_residents(self):
        return self.residents


class JustinTests(unittest.TestCase):
    def test_get_all_residents(self):
        citadel = Citadel()
        residents = citadel.get_add_residents()
        self.assertCountEqual(residents, [])


if __name__ == '__main__':
    unittest.main()

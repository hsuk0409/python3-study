import unittest

from rick_test import Rick


class Citadel(object):
    def __init__(self):
        self._residents = []

    def get_all_residents(self):
        return self._residents

    def add_resident(self, resident):
        self._residents.append(resident)


class Morty(object):
    def __init__(self, universe):
        self._residents = []
        self.universe = universe

    def get_all_residents(self):
        return self._residents

    def add_resident(self, resident):
        self._residents.append(resident)


class CitadelTests(unittest.TestCase):
    def test_get_all_residents(self):
        citadel = Citadel()
        residents = citadel.get_all_residents()
        self.assertCountEqual(residents, [])

    def test_add_residents(self):
        citadel = Citadel()
        rick = Rick(111)
        morty = Morty(111)

        citadel.add_resident(rick)
        citadel.add_resident(morty)
        residents = citadel.get_all_residents()

        self.assertEqual(residents[0], rick)
        self.assertEqual(residents[1], morty)


if __name__ == '__main__':
    unittest.main()

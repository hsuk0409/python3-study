import unittest

from my_array import MyArray


class TestArray(unittest.TestCase):
    def test_sum(self):
        arr = MyArray()
        result = arr.sum(5, '1 2 3 4 10 12')
        self.assertEqual(result, 32)

    def test_sum_raise_exception(self):
        self.assertRaises(Exception, lambda: MyArray.sum(5, '1 2 3 4 10 12'))

    # def tearDown(self):
    #     print('배열에 요소 = {}'.format(self.array))

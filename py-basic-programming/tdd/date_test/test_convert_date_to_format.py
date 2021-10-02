import unittest

import convert_date_to_format


class TestConvertDateToFormat(unittest.TestCase):

    def test_convert_date_to_format(self):
        date_string = '20211002'
        formatted_date = '2021-10-02'

        result = convert_date_to_format.convert_date_to_formatted_string(date_string)
        print(f"result=={result}!!")
        print(f"result date=={result}!!")
        print(f"result type=={type(result)}!!")
        print(f"result date type=={type(result)}!!")
        print(f"string result=={result}!!")
        self.assertEqual(result, formatted_date)

    def test_wrong_string_date(self):
        wrong_date = '2021122222222222222222'
        zero_date = '0'
        wrong_result = convert_date_to_format.convert_date_to_formatted_string(wrong_date)

        self.assertEqual(wrong_result, "")
        self.assertEqual(zero_date, "0")


if __name__ == '__main__':
    unittest.main()

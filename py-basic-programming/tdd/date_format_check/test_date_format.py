import unittest
from datetime import datetime


def validate(date_text) -> bool:
    try:
        datetime.strptime(date_text, "%y%m%d")
        return True
    except ValueError:
        raise ValueError("올바른 날짜 형식이 아닙니다.")


class TestDateFormat(unittest.TestCase):
    def check_date_format(self):
        wrong_date = "2021-09-24"
        right_date = "20210924"

        self.assertRaises(validate(wrong_date), ValueError)
        self.assertTrue(validate(right_date))


if __name__ == "__main__":
    unittest.main()

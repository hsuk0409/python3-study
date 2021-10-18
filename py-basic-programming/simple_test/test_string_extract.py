import re
import unittest


class TestStringExtract(unittest.TestCase):

    def test_number_from_string(self) -> None:
        tmp_str = "5j9u04t5i9n09"
        num_str = re.sub(r'[^0-9]', '', tmp_str)
        print(f"string num: {num_str}")

        self.assertEqual(num_str, "59045909")


if __name__ == "__main__":
    unittest.main()

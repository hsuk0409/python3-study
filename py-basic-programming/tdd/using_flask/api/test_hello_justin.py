import json
import unittest

import backend


class TestHelloJustin(unittest.TestCase):
    def setUp(self) -> None:
        self.host = "http://localhost:5000"
        self.app = backend.app.test_client()
        self.right_param = {
            "param1": 5,
            "param2": 10
        }
        self.wrong_param = {
            "param1": 20
        }

    def test_multiply_right(self):
        res = self.app.get(self.host + "/api/multiply", data=self.right_param)
        data = json.loads(res.get_data())
        self.assertEqual(50, data["response"])
        self.assertEqual(1, data["state"])

    def test_wrong_param(self):
        res = self.app.get(self.host + "/api/multiply", data=self.wrong_param)
        data = json.loads(res.get_data())
        self.assertEqual(None, data["response"])
        self.assertEqual(0, data["state"])


if __name__ == "__main__":
    unittest.main()

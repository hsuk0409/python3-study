import unittest

from api import backend


class TestHelloJustin(unittest.TestCase):
    def setUp(self) -> None:
        self.domain = "http://localhost:5000/api/multiply"

    def test_mul(self):
        self.assertEqual(50, backend.multiply(5, 10))

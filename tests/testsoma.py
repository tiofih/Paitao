import unittest
from primeiro import soma


class TestSoma(unittest.TestCase):
    def teste_retono_soma(self):
        self.assertEqual(soma(10, 10), 20)

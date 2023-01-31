import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.operations = { "+" : add, "-" : subtract, "*" : multiply, "/" : divide }

    def test_addition(self):
        result = self.operations['+'](2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = self.operations['-'](3, 2)
        self.assertEqual(result, 1)

    def test_multiplication(self):
        result = self.operations['*'](2, 3)
        self.assertEqual(result, 6)

    def test_division(self):
        result = self.operations['/'](6, 3)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = subtract(3, 2)
        self.assertEqual(result, 1)

    def test_multiplication(self):
        result = multiply(2, 3)
        self.assertEqual(result, 6)

    def test_division(self):
        result = divide(6, 3)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()

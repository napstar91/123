import unittest
import io
import sys

class TestPizzaOrdering(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, io.StringIO()

    def test_small_pizza(self):
        # arrange
        sys.stdin = io.StringIO("S\nN\nN\n")

        # act
        exec(self.input_str)

        # assert
        output = sys.stdout.getvalue()
        self.assertIn("Your final bill is $15", output)

    def test_medium_pizza_with_pepperoni(self):
        # arrange
        sys.stdin = io.StringIO("M\nY\nN\n")

        # act
        exec(self.input_str)

        # assert
        output = sys.stdout.getvalue()
        self.assertIn("Your final bill is $23", output)

    def test_large_pizza_with_pepperoni_and_extra_cheese(self):
        # arrange
        sys.stdin = io.StringIO("L\nY\nY\n")

        # act
        exec(self.input_str)

        # assert
        output = sys.stdout.getvalue()
        self.assertIn("Your final bill is $29", output)

    def tearDown(self):
        sys.stdout = self.held

if __name__ == '__main__':
    unittest.main()

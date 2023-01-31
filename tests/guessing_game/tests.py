import unittest
import io
import sys
from random import randint

class TestNumberGuessingGame(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, io.StringIO()

    def test_easy_mode(self):
        # arrange
        answer = randint(1,100)
        sys.stdin = io.StringIO(f"easy\n{answer}\n")

        # act
        game()

        # assert
        output = sys.stdout.getvalue()
        self.assertIn(f"You got it! The answer was {answer}", output)

    def test_hard_mode(self):
        # arrange
        answer = randint(1,100)
        sys.stdin = io.StringIO(f"hard\n{answer}\n")

        # act
        game()

        # assert
        output = sys.stdout.getvalue()
        self.assertIn(f"You got it! The answer was {answer}", output)

    def test_lose(self):
        # arrange
        answer = randint(1,100)
        sys.stdin = io.StringIO(f"easy\n{answer+1}\n{answer+2}\n{answer+3}\n{answer+4}\n{answer+5}\n{answer+6}\n{answer+7}\n{answer+8}\n{answer+9}\n{answer+10}\n")

        # act
        game()

        # assert
        output = sys.stdout.getvalue()
        self.assertIn("Game over, you ran out of guesses", output)

    def tearDown(self):
        sys.stdout = self.held

if __name__ == '__main__':
    unittest.main()

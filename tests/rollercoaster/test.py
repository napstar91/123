import unittest

class TestRollerCoaster(unittest.TestCase):
    def test_height_check(self):
        height = 150
        result = roller_coaster(height)
        self.assertEqual(result, "You can go on the ride!")

        height = 100
        result = roller_coaster(height)
        self.assertEqual(result, "Sorry, you are not tall enough to go on this ride.")

    def test_age_check(self):
        height = 150
        age = 8
        result = roller_coaster(height, age)
        self.assertEqual(result, "Your ticket price is $5")

        age = 15
        result = roller_coaster(height, age)
        self.assertEqual(result, "Your ticket price is $12")

        age = 20
        result = roller_coaster(height, age)
        self.assertEqual(result, "Your ticket price is $7")

    def test_photo_check(self):
        height = 150
        age = 20
        wants_photo = "Y"
        result = roller_coaster(height, age, wants_photo)
        self.assertEqual(result, "Your final bill is $10")

        wants_photo = "N"
        result = roller_coaster(height, age, wants_photo)
        self.assertEqual(result, "Your ticket price is $7")

if __name__ == '__main__':
    unittest.main()

# Test case 1: Height is greater than 120 cm and age is less than 12
input_height = 121
input_age = 11
input_photo = "Y"
expected_output = "You can go on the ride.\nYour ticket is 5$.\nYour bill is 8$.\n"

# Test case 2: Height is greater than 120 cm and age is between 12 and 18
input_height = 121
input_age = 15
input_photo = "N"
expected_output = "You can go on the ride.\nYour ticket is 12$.\n"

# Test case 3: Height is greater than 120 cm and age is greater than 18
input_height = 121
input_age = 22
input_photo = "Y"
expected_output = "You can go on the ride.\nYour ticket is 7$.\nYour bill is 10$.\n"

# Test case 4: Height is less than or equal to 120 cm
input_height = 120
input_age = 22
input_photo = "Y"
expected_output = "Sorry, you're not tall enough to go on the ride.\n"

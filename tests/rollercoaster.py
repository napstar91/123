def test_roller_coaster():
    # Test 1: Height less than 120 cm
    height = 119
    result = run_roller_coaster(height)
    assert result == "Sorry, you are not tall enough to go on this ride.", f"Expected 'Sorry, you are not tall enough to go on this ride.' but got {result}"

    # Test 2: Height equal to or greater than 120 cm, age less than 12, no photo
    height = 120
    age = 11
    wants_photo = "N"
    result = run_roller_coaster(height, age, wants_photo)
    assert result == "Your ticket price is $5\n", f"Expected 'Your ticket price is $5\n' but got {result}"

    # Test 3: Height equal to or greater than 120 cm, age between 12 and 18, no photo
    height = 130
    age = 16
    wants_photo = "N"
    result = run_roller_coaster(height, age, wants_photo)
    assert result == "Your ticket price is $12\n", f"Expected 'Your ticket price is $12\n' but got {result}"

    # Test 4: Height equal to or greater than 120 cm, age greater than 18, with photo
    height = 140
    age = 19
    wants_photo = "Y"
    result = run_roller_coaster(height, age, wants_photo)
    assert result == "Your ticket price is $7\nYour final bill is $10\n", f"Expected 'Your ticket price is $7\nYour final bill is $10\n' but got {result}"

def run_roller_coaster(height, age=None, wants_photo=None):
    result = f"Welcome to the Roller Coaster!\nWhat is your height (in cm)? {height}\nYou can go on the ride!\n"
    if age:
        result += f"What is your age? {age}\n"
    if age and age < 12:
        result += "Your ticket price is $5\n"
    elif age and age <= 18:
        result += "Your ticket price is $12\n"
    else:
        result += "Your ticket price is $7\n"
    if wants_photo:
        result += f"Do you want a photo taken? (Y/N) {wants_photo}\n"
    if wants_photo and wants_photo.upper() == "Y":
        result += "Your final bill is $10\n"
    return result

test_roller_coaster()

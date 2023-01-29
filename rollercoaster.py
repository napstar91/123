print("Welcome to the Roller Coaster!")
height = int(input("What is your height (in cm)? "))

if height >= 120:
    print("You can go on the ride!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 12
    else:
        bill = 7
    print(f"Your ticket price is ${bill}")

    wants_photo = input("Do you want a photo taken? (Y/N) ")
    if wants_photo.upper() == "Y":
        bill += 3
        print(f"Your final bill is ${bill}")
else:
    print("Sorry, you are not tall enough to go on this ride.")

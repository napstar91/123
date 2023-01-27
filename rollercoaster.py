print ("welcome to rollercoaster")
height = int (input ("what is your height "))
bill = 0
if height > 120:
    print ("You can go")
    age =  int(input ("What is you age "))
    if age < 12:
        bill = 5
        print ("Your ticket is 5%")
    elif age <= 18:
        bill = 12
        print ("Your ticket is 12$")
    else:
        bill = 7
        print ("Your ticket is 7")
    wants_photo = input ("Do u want photo taken? Y or N ")
    if wants_photo == "Y":
        bill +=3
        print (f"Your bill is {bill}")

else:
    print ("You can't go")

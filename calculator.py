# utensils = {"fork","spoon","knife","knife","knife"}
# dishes = {"bowl","plate","cup"}
# utensils.add("napkin")
# utensils.remove("napkin")
# utensils.update(dishes)
# for x in utensils:
#     print (x)

#index operator
# name = "bro CODE!"
# # if (name[0].islower()):
# #     name = name.capitalize()
# # first_name = name[0:3].upper()
# # last_name = name[4:].lower()
# last_character = name[-1]
# print(last_character)



# def multiply (number1,number2):
#     return number1 * number2
# x = multiply(6,8)
# print (x)

#nested function
# print(round(abs(float(input("Enter a whole number")))))from art import cal
from art import logo
def add (n1,n2):
    return n1 + n2
def subtract (n1,n2):
    return n1 + n2
def multiply (n1,n2):
    return (n1*n2)
def divide (n1,n2):
    return (n1/n2)

operations = { "+" : add, "-" : subtract, "*" : multiply, "/" : "divide"
}

num1 = float(input("Enter first number "))
num2 = float(input("Enter second number "))
for symbol in operations:
    print (symbol)
operation_symbol = input ("Pick an operation from the lince above")
calculation_function = operations[operation_symbol]
answer = calculation_function (num1,num2)

print (f"{num1} {operation_symbol} {num2} ={answer}")
print (logo)
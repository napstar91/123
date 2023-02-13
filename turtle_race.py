from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title = "make your bet", prompt= "which turtle will win the race? Enter color:")
y_positions = [-100, -80, -60, -40, -20]
colors = ["green", "red", "blue", "orange","black"]
all_turtles = []


for turtle_index in range (0,5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print (f"You've won, the {winning_color} turtle is winner")
            else:
                print (f"You'vee lost,the {winning_color} turtle is winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()

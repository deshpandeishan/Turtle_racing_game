from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

screen.title("Welcome to turtle race!")
color_set = (113, 231, 247)
hex_color = "#{:02x}{:02x}{:02x}".format(*color_set)    # Converts into supportable format.
screen.bgcolor(hex_color)

user_bet = screen.textinput(title="Enter your bet", prompt="Choose the color of the turtle that you think will win the race:" )
colors_list = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
y_coordinates = [-100, -50, 0, 50, 100, 150]

turtles = []

for _ in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors_list[_])
    new_turtle.penup()
    new_turtle.goto(-230, y_coordinates[_])
    turtles.append(new_turtle)

race_on = True
while race_on:
    for turtle in turtles:
        random_distance = randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 220:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")

screen.exitonclick()

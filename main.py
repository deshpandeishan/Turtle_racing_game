import turtle
from random import randint

screen = turtle.Screen()
screen.setup(width=1000, height=1000)


screen.bgcolor("#92B6F5")
screen.title("Welcome to the turtle race!")

kasav = turtle.Turtle()
kasav.penup()
kasav.hideturtle()
kasav.speed(0)

turtle.tracer(False)

square_size = 10

for i in range(0, 30, square_size):
    for j in range(0, 430, square_size):
        if (i // square_size + j // square_size) % 2 == 0:
            kasav.fillcolor("white")
        else:
            kasav.fillcolor("black")
        kasav.penup()
        kasav.goto(i + 250, j + -200)
        kasav.pendown()
        kasav.begin_fill()
        for _ in range(4):
            kasav.forward(square_size)
            kasav.right(90)
        kasav.end_fill()

turtle.update()


turtle.tracer(True)
turtle.speed(10)
screen.title("Welcome to turtle race!")
color_set = (113, 231, 247)
hex_color = "#{:02x}{:02x}{:02x}".format(*color_set)
screen.bgcolor(hex_color)

user_bet = screen.textinput(title="Enter your bet", prompt="Choose the color of the turtle that you think will win the race:" )
colors_list = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
y_coordinates = [-100, -50, 0, 50, 100, 150]

turtles = []

for _ in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
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

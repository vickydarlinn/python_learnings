from turtle import Turtle, Screen
import random
timmy_the_turtle = Turtle()
my_screen = Screen()


# print(timmy_the_turtle)
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)

#
# for i in range(7):
#     for _ in range(i + 2):
#         timmy_the_turtle.color("red")
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360 / (i + 2))

colors = ["red", "green", "black", "blue", "yellow", "purple", "wheat"]
directions = [0, 90, 180, 270]
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

for _ in range(200):
    timmy_the_turtle.forward(40)
    timmy_the_turtle.color(random.choice(colors))
    timmy_the_turtle.setheading(random.choice(directions))

my_screen.exitonclick()


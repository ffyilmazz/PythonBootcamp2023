# import modules
import turtle
# resources:
# 1- https://docs.python.org/3/library/turtle.html
# 2- https://cs111.wellesley.edu/reference/colors

# creating an object from class
timmy = turtle.Turtle()
print(timmy)

# methods belong to created object
timmy.color("coral")
timmy.shape("turtle")
timmy.forward(100)

my_screen = turtle.Screen()

# accessing attributes
print(my_screen.canvheight)

# methods belong to created object
my_screen.exitonclick()
import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
my_turtle = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
my_turtle.shape('turtle')
# Set your turtle's speed using .speed(2)
my_turtle.speed(2)
# Set your turtle's color using .color('green') and .pencolor('blue')
my_turtle.color('green')
my_turtle.pencolor('blue')
# Move your turtle forward using .forward(100)
my_turtle.forward(100)
# TEST    Did your turtle move forward?
# Yes.
# Move your turtle left or right using .left(90) or .right(90)
my_turtle.left(90)
my_turtle.right(90)
# Now put the forward and left/right code into a for loop to repeat 4 times.
for x in range(4):
    my_turtle.right(90)
    my_turtle.forward(100)

# TEST    Did your turtle draw a square?
#yes.
# Move your turtle to a new place on the screen using .goto(x,y)
my_turtle.goto(0,0)
# x=0 and y=0 is the center of the screen
my_turtle.color('green')
my_turtle.begin_fill()

# Have your turtle draw a circle using .circle(radius, steps=30)
my_turtle.circle(10, steps=30)
#for x in range(3`60):
   # my_turtle.right(1)
   # my_turtle.forward(1)
# TEST    Did your turtle draw a circle?

# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below
my_turtle.end_fill()
my_turtle.goto(10,10)
my_turtle.circle(100, steps=30)
# Draw 3 more shapes with different fill colors!

my_turtle.color("blue")
my_turtle.begin_fill()
for p in range(6):
    my_turtle.forward(100)
    my_turtle.left(60)
my_turtle.end_fill()
my_turtle.color("pink")
my_turtle.begin_fill()
for p in range(3):
    my_turtle.forward(100)
    my_turtle.right(120)
my_turtle.end_fill()
my_turtle.color("yellow")
my_turtle.begin_fill()
for p in range(10):
    my_turtle.forward(100)
    my_turtle.right(36)
my_turtle.end_fill()
# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()

# A Pong game constructed in Python 3
# via freecodecamp

import turtle

wn = turtle.Screen()
wn.title("A pong game by @mjkonko")
wn.bgcolor("white")
wn.setup(width=1000, height=800)
wn.tracer(0)

#Paddle left
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("black")
paddle_left.shapesize(stretch_wid=7,stretch_len=1)
paddle_left.penup()
paddle_left.goto(-480,0)

#Paddle right
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("black")
paddle_right.shapesize(stretch_wid=7,stretch_len=1)
paddle_right.penup()
paddle_right.goto(480,0)


#Ball

#Main loop

while True:
    wn.update()


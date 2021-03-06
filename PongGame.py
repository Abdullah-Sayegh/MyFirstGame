from pickle import TRUE
from tkinter import W
import turtle

wind = turtle.Screen()
wind.title("My FIrst Pong Game")
wind.bgcolor("black")
wind.setup(height=600, width=800)
wind.tracer(0)

madrab1= turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("red")
madrab1.penup()
madrab1.goto(-350, 0)
madrab1.shapesize(stretch_wid=7, stretch_len=1)


madrab2= turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("yellow")
madrab2.penup()
madrab2.goto(350, 0)
madrab2.shapesize(stretch_wid=7, stretch_len=1)


ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 Player 2: 0", align="center", font="arial")



def MoveUp1():
    y=madrab1.ycor()
    y +=20
    madrab1.sety(y)

def MoveDown1():
    y=madrab1.ycor()
    y -=20
    madrab1.sety(y)

wind.listen()
wind.onkeypress(MoveUp1, "w")
wind.onkeypress(MoveDown1, "s")


def MoveUp2():
    y=madrab2.ycor()
    y +=20
    madrab2.sety(y)

def MoveDown2():
    y=madrab2.ycor()
    y -=20
    madrab2.sety(y)

wind.listen()
wind.onkeypress(MoveUp2, "Up")
wind.onkeypress(MoveDown2, "Down")

while True:
    wind.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() >390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font="arial")

    if ball.xcor() <-390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font="arial")
    
    if (ball.xcor() > 340 and ball.xcor() < 360) and (ball.ycor() < madrab2.ycor() + 90 and ball.ycor() > madrab2.ycor() - 90):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -360) and (ball.ycor() < madrab1.ycor() + 90 and ball.ycor() > madrab1.ycor() - 90):
        ball.setx(-340)
        ball.dx *= -1

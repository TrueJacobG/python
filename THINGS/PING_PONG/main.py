import turtle as t
import os

playerScore1 = 0
playerScore2 = 0

win = t.Screen()
win.title("Pong Game!")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# paddles
leftPaddle = t.Turtle()
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("white")
leftPaddle.shapesize(stretch_wid=5, stretch_len=1)
leftPaddle.penup()
leftPaddle.goto(-350, 0)

rightPaddle = t.Turtle()
rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.shapesize(stretch_wid=5, stretch_len=1)
rightPaddle.color("grey")
rightPaddle.penup()
rightPaddle.goto(350, 0)


# ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ballxdir = 0.2
ballydir = 0.2


# scoreboard
scoreboard = t.Turtle()
scoreboard.speed(0)
scoreboard.color("blue")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Score", align="center", font=("Arial", 32, "normal"))


def leftPaddleUp():
    y = leftPaddle.ycor()
    y += 20
    leftPaddle.sety(y)


def leftPaddleDown():
    y = leftPaddle.ycor()
    y -= 20
    leftPaddle.sety(y)


def rightPaddleUp():
    y = rightPaddle.ycor()
    y += 20
    rightPaddle.sety(y)


def rightPaddleDown():
    y = rightPaddle.ycor()
    y -= 20
    rightPaddle.sety(y)


win.listen()
win.onkeypress(leftPaddleUp, key="w")
win.onkeypress(leftPaddleDown, key="s")
win.onkeypress(rightPaddleUp, key="Up")
win.onkeypress(rightPaddleDown, key="Down")


while True:
    win.update()

    ball.setx(ball.xcor() + ballxdir)
    ball.sety(ball.ycor() + ballydir)

    if ball.ycor() > 290:
        ball.sety(290)
        ballydir *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ballydir *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ballxdir *= -1
        playerScore1 += 1
        scoreboard.clear()
        scoreboard.write(f"Player 1: {playerScore1} Player 2: {playerScore2}", align="center", font=(
            "Arial", 32, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ballxdir *= -1
        playerScore1 += 1
        scoreboard.clear()
        scoreboard.write(f"Player 1: {playerScore1} Player 2: {playerScore2}", align="center", font=(
            "Arial", 32, "normal"))

    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightPaddle.ycor() + 40 and ball.ycor() > rightPaddle.ycor() - 40):
        ball.setx(340)
        ballxdir = ballxdir * -1

    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftPaddle.ycor() + 40 and ball.ycor() > leftPaddle.ycor() - 40):
        ball.setx(-340)
        ballxdir = ballxdir * -1

import turtle
from random import choice

windows = turtle.Screen()
windows.title('Ping-Pong')
windows.bgcolor("black")
windows.setup(width=1.0, height=1.0)
windows.tracer(2)
abc = turtle.Turtle(visible=False)
FONT =("Arial",44)
igrok_1 = 0
igrok_2 = 0
abc.color("white")
abc.up()
abc.setposition(-200,300)
abc.write(igrok_1, font=FONT)
abc2 = turtle.Turtle(visible=False)
abc2.color("white")
abc2.up()
abc2.setposition(200,300)
abc2.write(igrok_1, font=FONT)

table = turtle.Turtle()
table.color("green")
table.speed(0)
table.begin_fill()
table.goto(-500, 300)
table.goto(500, 300)
table.goto(500, -300)
table.goto(-500, -300)
table.goto(-500, 300)
table.end_fill()
table.goto(0, 300)
table.color("red")
table.setheading(270)
for i in range(25):
    if i % 2 == 0:
        table.forward(24)
    else:
        table.up()
        table.forward(24)
        table.down()
table.hideturtle()

play = turtle.Turtle()
play.color("black")
play.shape("square")
play.shapesize(stretch_wid=5, stretch_len=1)
play.penup()
play.goto(-450, 0)

play_a = turtle.Turtle()
play_a.color("black")
play_a.shape("square")
play_a.shapesize(stretch_wid=5, stretch_len=1)
play_a.penup()
play_a.goto(450, 0)


def move_up():
    y = play.ycor() + 10
    if y > 250:
        y = 250
    play.sety(y)


def move_down():
    y = play.ycor() - 10
    if y < -250:
        y = -250
    play.sety(y)


def move_up_b():
    y = play_a.ycor() + 10
    if y > 250:
        y = 250
    play_a.sety(y)


def move_down_b():
    y = play_a.ycor() - 10
    if y < -250:
        y = -250
    play_a.sety(y)


boll = turtle.Turtle()
boll.speed(0)
boll.shape("circle")

boll.shapesize(stretch_wid=1, stretch_len=1)
boll.up()
boll.dx = 3
boll.dy = -3

windows.listen()
windows.onkeypress(move_up, 'w')
windows.onkeypress(move_down, 's')
windows.onkeypress(move_up_b, 'Up')
windows.onkeypress(move_down_b, 'Down')

while True:
    windows.update()
    boll.setx(boll.xcor() + boll.dx)
    boll.sety(boll.ycor() + boll.dy)

    if boll.ycor() >= 290:
        boll.dy = -boll.dy

    if boll.ycor() <= -290:
        boll.dy = -boll.dy

    if boll.xcor() >= 490:
        igrok_1 += 1
        abc.clear()
        abc.write(igrok_1, font=FONT)
        boll.goto(0, 0)
        boll.dx = choice([-1, -2, -3, -4, -5])
        boll.dy = choice([-1, -2, -3, -4, -5])

    if boll.xcor() <= -490:
        igrok_2 += 1
        abc2.clear()
        abc2.write(igrok_2, font=FONT)
        boll.goto(0, 0)
        boll.dx = choice([-1, -2, -3, -4, -5])
        boll.dy = choice([-1, -2, -3, -4, -5])

    if boll.ycor() >= play_a.ycor() - 50 and boll.ycor() <= play_a.ycor() + 50 \
            and boll.xcor() >= play_a.xcor() - 5 and boll.xcor() <= play_a.xcor() + 5:
        boll.dx = -boll.dx
    if boll.ycor() >= play.ycor() - 50 and boll.ycor() <= play.ycor() + 50 \
            and boll.xcor() >= play.xcor() - 5 and boll.xcor() <= play.xcor() + 5:
        boll.dx = -boll.dx

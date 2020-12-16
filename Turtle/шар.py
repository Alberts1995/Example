import turtle

windows = turtle.Screen()
windows.title('мячь')
play = turtle.Turtle()
play.speed(0)
play.up()
play.goto(300, 300)
play.down()
play.hideturtle()
play.pensize(8)
play.color("yellow")
play.goto(300, -300)
play.goto(-300, -300)
play.goto(-300, 300)
play.goto(300, 300)

bool = turtle.Turtle()
bool.shape("circle")
bool.color("red")
bool.up()

dx = 3
dy = 2
while True:
    x, y = bool.position()
    if x + dx >= 300 or x + dx <= -300:
        dx = -dx
    if y + dy >= 300 or y + dy <= -300:
        dy = -dy

    bool.goto(x + dx, y+dy)

windows.mainloop

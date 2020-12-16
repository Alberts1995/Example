import turtle

windows = turtle.Screen()
windows.title("окно ")

evropa = turtle.Turtle()
africa = turtle.Turtle()
america = turtle.Turtle()
asia = turtle.Turtle()
avstraliya = turtle.Turtle()

for i in[evropa,africa,america,asia,avstraliya]:
    i.up()

evropa.goto(-100,100)
africa.goto(0,100)
america.goto(100,100)
asia.goto(-50,50)
avstraliya.goto(50,50)

for i in[evropa,africa,america,asia,avstraliya]:
    i.down()
evropa.color("blue")
africa.color("black")
america.color("red")
asia.color("yellow")
avstraliya.color("green")
for i in[evropa,africa,america,asia,avstraliya]:
    i.circle(50)

windows.mainloop()

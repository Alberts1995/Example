import turtle

windows = turtle.Screen()
windows.title('графика')
windows.setup(width=1.0,height=1.0)
abc = turtle.Turtle(visible=False)
abc.speed(50)


colors = ["red", "green", "blue", "black"]


def sq(a):
    for i in range(4):
        abc.color(colors[i % 4])
        abc.forward(a)
        abc.left(90)



dlinna = 40
for i in range(40):
    abc.color(colors[i % 4])
    sq(dlinna)
    abc.left(10)
    dlinna = dlinna + 7

windows.mainloop()

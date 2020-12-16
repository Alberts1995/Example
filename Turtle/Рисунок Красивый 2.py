import turtle

window = turtle.Screen()
pla = turtle.Turtle()
window.bgcolor("black")
pla.speed(0)
color = ["Red", "Yellow", "Green", "Blue"]
for x in range(360):
    pla.pencolor(color[x % 4])
    pla.circle(x)
    pla.left(90)
window.mainloop()

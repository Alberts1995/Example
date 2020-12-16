import turtle

window = turtle.Screen()
window.title("Рисоунок 1")
turtle.shape("turtle")
turtle.color('red')


def start(n, dlinna):
    if n % 2 != 0:
        for i in range(n):
            turtle.forward(dlinna)
            afx = n // 2 * 360 / n
            turtle.left(afx)


start(5, 100)

window.mainloop()

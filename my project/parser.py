import bs4
import requests
from tkinter import Tk, mainloop, Button, Entry, Label


def output(event):
    txt = entery.get()
    data = "https://sinoptik.com.ru/погода-{}".format(txt)
    s = requests.get(data)
    b = bs4.BeautifulSoup(s.text, "html.parser")

    # 1 столбик
    s4 = b.select(".table__col .table__time_hours")
    test = str(s4)
    time = s4[2].getText()
    s3 = b.select(".table__col .table__temp")
    test = str(s3)
    temp = s3[2].getText()
    s2 = b.select(".table__col .table__pressure")
    test = str(s2)
    dovlen = s2[2].getText()
    s1 = b.select(".table__col .table__humidity")
    test = str(s1)
    vlaz = s1[2].getText()
    

    # 2 столбик
    p4 = b.select(".table__col .table__time_hours")
    test = str(p4)
    time1 = p4[4].getText()
    p3 = b.select(".table__col .table__temp")
    test = str(p3)
    temp1 = p3[4].getText()
    p2 = b.select(".table__col .table__pressure")
    test = str(p2)
    dovlen1 = p2[4].getText()
    p1 = b.select(".table__col .table__humidity")
    test = str(p1)
    vlaz1 = p1[4].getText()

    # 3 столбик
    c4 = b.select(".table__col .table__time_hours")
    test = str(c4)
    time2 = c4[6].getText()
    c3 = b.select(".table__col .table__temp")
    test = str(c3)
    temp2 = c3[6].getText()
    c2 = b.select(".table__col .table__pressure")
    test = str(c2)
    dovlen2 = c2[6].getText()
    c1 = b.select(".table__col .table__humidity")
    test = str(c1)
    vlaz2 = c1[6].getText()
    

    # 1 информация
    tims["text"] =  time
    temps["text"] =  "Температура:", temp
    dovlens["text"] = "Довление:", dovlen, "мм"
    vlazs["text"] = "Влажность:", vlaz, "%"
    
    # 2 информация
    tims1["text"] =  time1
    temps1["text"] = "Температура:", temp1
    dovlens1["text"] = "Довление:", dovlen1, "мм"
    vlazs1["text"] = "Влажность:", vlaz1, "%"

    # 3 информация    
    tims2["text"] =  time2
    temps2["text"] = "Температура:", temp2
    dovlens2["text"] = "Довление:", dovlen2, "мм"
    vlazs2["text"] = "Влажность:", vlaz2, "%"

w1 = Tk()
w1.geometry('400x200')
w1.title("Weather")

entery = Entry(w1, width=15, font=29, fg="green")
entery.config(font = ("Times", 13))
button = Button(w1, text="Поиск",)
button.config(font = ("Times", 9))
lable1 = Label(w1, text="Введи название города", fg="black")
lable1.config(font = ("Times", 15))

temps = Label(w1, fg="black")
dovlens = Label(w1, fg="black")
vlazs = Label(w1, fg="black")
veters = Label(w1, fg="black")
tims = Label(w1, fg="black")

temps1 = Label(w1, fg="black")
dovlens1 = Label(w1, fg="black")
vlazs1 = Label(w1, fg="black")
veters1 = Label(w1, fg="black")
tims1 = Label(w1, fg="black")

temps2 = Label(w1, fg="black")
dovlens2 = Label(w1, fg="black")
vlazs2 = Label(w1, fg="black")
veters2 = Label(w1, fg="black")
tims2 = Label(w1, fg="black")

button.place(x=140, y=22)
lable1.place(x=0, y=0)
entery.place(x=0, y=25)

temps.place(x=0, y=85)
dovlens.place(x=0, y=105)
vlazs.place(x=0, y=125)
veters.place(x=0, y=140)
tims.place(x=0, y=50)

temps1.place(x=120, y=85)
dovlens1.place(x=120, y=105)
vlazs1.place(x=120, y=125)
veters1.place(x=120, y=140)
tims1.place(x=120, y=50)

temps2.place(x=250, y=85)
dovlens2.place(x=250, y=105)
vlazs2.place(x=250, y=125)
veters2.place(x=250, y=140)
tims2.place(x=250, y=50)


button.bind("<Button-1>", output)
w1.mainloop()









from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import sys


class Ui_Weawer(object):
    def setupUi(self, Weawer):
        Weawer.setObjectName("Weawer")
        Weawer.resize(342, 376)
        Weawer.setStyleSheet("background-color: rgb(129, 197, 117);")
        self.pushButton = QtWidgets.QPushButton(Weawer)
        self.pushButton.setGeometry(QtCore.QRect(0, 60, 75, 23))
        self.pushButton.setStyleSheet("QPushButtom{\n"
"rgb(93, 131, 255)\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Weawer)
        self.label.setGeometry(QtCore.QRect(0, 95, 251, 31))
        self.label.setStyleSheet("font: 75 16pt \"Segoe Script\";")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Weawer)
        self.lineEdit.setGeometry(QtCore.QRect(0, 30, 251, 31))
        self.lineEdit.setStyleSheet("color :rgb(216, 58, 255);\n"
"font: 12pt \"Viner Hand ITC\";\n"
"background-color : rgb(255, 240, 245);\n"
"border : no;\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Weawer)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 181, 21))
        self.label_2.setToolTipDuration(-7)
        self.label_2.setStyleSheet("font: 75 12pt \"Segoe Print\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Weawer)
        self.label_3.setGeometry(QtCore.QRect(0, 140, 341, 241))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("EWNW.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Weawer)
        QtCore.QMetaObject.connectSlotsByName(Weawer)

    def retranslateUi(self, Weawer):
        _translate = QtCore.QCoreApplication.translate
        Weawer.setWindowTitle(_translate("weather", "Weather"))
        self.pushButton.setText(_translate("Weawer", "Искать"))
        self.label_2.setText(_translate("Weawer", "Впишите ваш город"))


app = QtWidgets.QApplication(sys.argv)
Weawer = QtWidgets.QDialog()
ui = Ui_Weawer()
ui.setupUi(Weawer)
Weawer.show()


def get_weather_city():
    txt = ui.lineEdit.text()
    respone = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=199fa8caaed78f8fe79860c384edacc7".format(txt)
    res = requests.get(respone)
    data = res.json()
    temp = data["main"]["temp"] - 273
    wind = data["wind"]["deg"]
    
    ui.label.setText(f"Темпертура: {round(temp)} C")
    if wind in range(0, 44):
        ui.label_3.setPixmap(QtGui.QPixmap("E.png"))
    elif wind in range(45, 89):
        ui.label_3.setPixmap(QtGui.QPixmap("NE.png"))
    elif wind  in range(90, 134):
        ui.label_3.setPixmap(QtGui.QPixmap("N.png"))
    elif wind  in range(135, 179):
        ui.label_3.setPixmap(QtGui.QPixmap("NW.png"))
    elif wind  in range(180, 224):
        ui.label_3.setPixmap(QtGui.QPixmap("W.png"))
    elif wind  in range(225, 269):
        ui.label_3.setPixmap(QtGui.QPixmap("SW.png"))
    elif wind  in range(270, 314):
        ui.label_3.setPixmap(QtGui.QPixmap("S.png"))
    elif wind  in range(314, 359):
        ui.label_3.setPixmap(QtGui.QPixmap("SE.png"))

ui.pushButton.clicked.connect(get_weather_city)
sys.exit(app.exec_())

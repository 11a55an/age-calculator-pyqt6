import sys
from datetime import date, datetime
from PyQt6.QtWidgets import QWidget, QApplication, QFormLayout, QPushButton, QDateEdit, QLineEdit, QLabel, QMainWindow

class MyMainWindow(QWidget):
    def __init__(self):
        super().__init__() #Initialize default constructor of parent class

        self.layout = QFormLayout()
        
        self.dateInput = QDateEdit()
        self.label = QLabel()
        self.label.setText("")
        self.button = QPushButton("Calculate")

        self.layout.addRow("Enter Your Birthdate: ", self.dateInput)
        self.layout.addRow(self.label)
        self.layout.addRow(self.button)

        self.setLayout(self.layout)
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.birthDate = self.dateInput.text()
        today = date.today()
        # print(self.today)
        self.dateStr = str(self.birthDate)
        # print(self.dateStr)
        dy, mt , yr = map(int, self.dateStr.split('/'))
        bDay = date(yr,mt,dy)
        # print(bDay)
        years = today.year - bDay.year
        months = today.month - bDay.month
        days = today.day - bDay.day
        if months < 0:
            months=((years*12)+months)%12
            years = years-1
        if days < 0:
            days = ((months*31)+days)%31
            months = months -1
        ageStr = "You are "+ str(years)+ " years, " +str(months)+ " months, "+str(days)+ " days old."
        self.label.setText(ageStr)
        # self.button.setEnabled(False)
application = QApplication(sys.argv)
window = MyMainWindow()
window.setWindowTitle("Age Calculator")

window.show()
application.exec()




    
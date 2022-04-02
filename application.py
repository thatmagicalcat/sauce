from PyQt5 import QtCore, QtGui, QtWidgets
import pyautogui
import os
from datetime import datetime
import utils

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(713, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 101, 21))
        self.label.setStyleSheet("font-size: 15px;\n"
"color: rgb(255, 0, 0)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 0, 101, 21))
        self.label_2.setStyleSheet("font-size: 15px;\n"
"color: rgb(255, 0, 0)")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 341, 21))
        self.lineEdit.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 30, 341, 21))
        self.lineEdit_2.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 62, 341, 41))
        self.pushButton.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;\n"
"background-color: rgb(255, 255, 255);\n"
"font-family: \"Hack Nerd Font Mono\";")
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 110, 691, 241))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 60, 161, 41))
        self.pushButton_2.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;\n"
"background-color: rgb(255, 255, 255);\n"
"font-family: \"Hack Nerd Font Mono\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 60, 171, 41))
        self.pushButton_3.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;\n"
"background-color: rgb(255, 255, 255);\n"
"font-family: \"Hack Nerd Font Mono\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 360, 691, 41))
        self.pushButton_4.setStyleSheet("border-radius: 5px;\n"
"border: 2px solid grey;\n"
"background-color: rgb(255, 255, 255);\n"
"font-family: \"Hack Nerd Font Mono\"")
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.local_list = {":date": f'{str(datetime.now().date()).replace("-", "/")}'}
        item_to_be_added = ":date" + " = " + self.local_list[":date"]
        self.listWidget.addItem(item_to_be_added)

        utils.add_abbreviation(self.local_list.items())
        self.pushButton.clicked.connect(self.main)

        self.pushButton_4.clicked.connect(self.remove_selected)

        self.pushButton_3.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(self.load)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Snippet:"))
        self.label_2.setText(_translate("MainWindow", "Text:"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.pushButton_2.setText(_translate("MainWindow", "Load"))
        self.pushButton_3.setText(_translate("MainWindow", "Save"))
        self.pushButton_4.setText(_translate("MainWindow", "Remove Selected"))

    def remove_selected(self):
        try:
            items_in_list = self.listWidget.selectedItems()
            utils.remove_abbrevation(self.local_list[items_in_list[0].text().split(" = ")[0]])
            del self.local_list[items_in_list[0].text().split(" = ")[0]]
            print(self.local_list)
            utils.add_abbreviation(self.local_list.items())

            if not items_in_list:
                pyautogui.alert("No item selected")
                return

            for item in items_in_list:
                self.listWidget.takeItem(self.listWidget.row(item))
        except Exception as e:
            pyautogui.alert(str(e))

    def main(self):
        if len(self.lineEdit.text()) != 0 and len(self.lineEdit_2.text()):
            for key, _ in self.local_list.items():
                utils.remove_abbrevation(key)

            item = self.lineEdit.text() + " = " + self.lineEdit_2.text()

            self.listWidget.addItem(item)
            self.local_list[item.split(" = ")[0]] = item.split(" = ")[1]

            self.lineEdit.setText("")
            self.lineEdit_2.setText("")

            utils.add_abbreviation(self.local_list.items())
        else:
            pyautogui.alert("Please enter something")

    def save(self):
        if os.path.isfile(".data"):
            os.remove(".data")

        with open(".data", "w") as file:
            for key, value in self.local_list.items():
                file.write(f"{key} = {value}\n")
            pyautogui.alert("Saved!")

    def load(self):
        pyautogui.alert("If you're seeing duplication of snippets, please restart the application and again load the file")
        if not os.path.isfile(".data"):
            pyautogui.alert("data file not exists")
            return
        
        with open(".data", "r") as file:
            lines = file.readlines()

            for line in lines:
                current_key, current_value = line.split(" = ")[0], line.split(" = ")[1]
                self.local_list[current_key] = current_value.replace("\n", "")
            
            self.listWidget.clear()

            for key, value in self.local_list.items():
                self.listWidget.addItem(f"{key} = {value}")

            utils.add_abbreviation(self.local_list.items())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

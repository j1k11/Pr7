# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desain.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(288, 279)
        MainWindow.setStyleSheet("background-color: grey;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(30, 10, 181, 83))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        font.setUnderline(True)
        self.title.setFont(font)
        self.title.setStyleSheet("color: black;")
        self.title.setObjectName("title")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(20, 80, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result.setFont(font)
        self.result.setStyleSheet("color: black;")
        self.result.setObjectName("result")
        self.cb_numbers = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_numbers.setGeometry(QtCore.QRect(10, 140, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_numbers.setFont(font)
        self.cb_numbers.setStyleSheet("color: black;")
        self.cb_numbers.setObjectName("cb_numbers")
        self.cb_alphabet = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_alphabet.setGeometry(QtCore.QRect(10, 140, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cb_alphabet.setFont(font)
        self.cb_alphabet.setStyleSheet("color: black;")
        self.cb_alphabet.setObjectName("cb_alphabet")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 200, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(" position: absolute;\n"
"    top:50%;\n"
"    background-color:#0a0a23;\n"
"    color: #fff;\n"
"    border:none;\n"
"    border-radius:10px;\n"
"    box-shadow: 0px 0px 2px 2px rgb(0,0,0);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Генератор паролів"))
        self.result.setText(_translate("MainWindow", "Тут буде результат "))
        self.cb_numbers.setText(_translate("MainWindow", "Використовувати числа"))
        self.cb_alphabet.setText(_translate("MainWindow", "Використовувати алфавіт"))
        self.pushButton.setText(_translate("MainWindow", "Згенерувати"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(611, 556)
        MainWindow.setStyleSheet("background-color: rgb(255, 230, 229);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SignInButton = QtWidgets.QPushButton(self.centralwidget)
        self.SignInButton.setGeometry(QtCore.QRect(180, 380, 271, 61))
        self.SignInButton.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"font: 75 18pt \"Arial\";")
        self.SignInButton.setObjectName("SignInButton")
        self.SignUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.SignUpButton.setGeometry(QtCore.QRect(180, 470, 271, 61))
        self.SignUpButton.setStyleSheet("background-color: rgb(255, 235, 84);\n"
"font: 75 18pt \"Arial\";")
        self.SignUpButton.setObjectName("SignUpButton")
        self.LoginTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.LoginTextEdit.setGeometry(QtCore.QRect(180, 200, 401, 51))
        self.LoginTextEdit.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(255, 212, 181);\n"
"border-color: rgb(85, 0, 0);")
        self.LoginTextEdit.setLineWidth(21)
        self.LoginTextEdit.setObjectName("LoginTextEdit")
        self.PasswordTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.PasswordTextEdit.setGeometry(QtCore.QRect(180, 290, 401, 51))
        self.PasswordTextEdit.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(255, 212, 181);\n"
"border-color: rgb(85, 0, 0);")
        self.PasswordTextEdit.setLineWidth(21)
        self.PasswordTextEdit.setObjectName("PasswordTextEdit")
        self.LoginLabel = QtWidgets.QLabel(self.centralwidget)
        self.LoginLabel.setGeometry(QtCore.QRect(50, 200, 71, 41))
        self.LoginLabel.setStyleSheet("font: 75 12pt \"Arial\";")
        self.LoginLabel.setObjectName("LoginLabel")
        self.PasswordLabel = QtWidgets.QLabel(self.centralwidget)
        self.PasswordLabel.setGeometry(QtCore.QRect(30, 290, 121, 41))
        self.PasswordLabel.setStyleSheet("font: 75 12pt \"Arial\";")
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.DrugStoreLabel = QtWidgets.QLabel(self.centralwidget)
        self.DrugStoreLabel.setGeometry(QtCore.QRect(70, 70, 461, 61))
        self.DrugStoreLabel.setStyleSheet("\n"
"font: 48pt \"Algerian\";")
        self.DrugStoreLabel.setObjectName("DrugStoreLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SignInButton.setText(_translate("MainWindow", "SIGN IN"))
        self.SignUpButton.setText(_translate("MainWindow", "SIGN UP"))
        self.LoginTextEdit.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Login</p></body></html>"))
        self.LoginLabel.setText(_translate("MainWindow", "LOGIN"))
        self.PasswordLabel.setText(_translate("MainWindow", "PASSWORD"))
        self.DrugStoreLabel.setText(_translate("MainWindow", "DRUG STORE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

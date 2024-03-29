# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegWindow(object):
    def setupUi(self, RegWindow):
        RegWindow.setObjectName("RegWindow")
        RegWindow.resize(597, 883)
        RegWindow.setStyleSheet(
            "QWidget {\n"
            "    background-color:rgb(82, 82, 82);\n"
            "}\n"
            "QDialog {\n"
            "    background-color:rgb(82, 82, 82);\n"
            "}\n"
            "QTextEdit {\n"
            "    background-color:rgb(42, 42, 42);\n"
            "    color: rgb(0, 255, 0);\n"
            "}\n"
            "QPushButton{\n"
            "    border-style: outset;\n"
            "    border-width: 2px;\n"
            "    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
            "    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
            "    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
            "    border-bottom-color: rgb(58, 58, 58);\n"
            "    border-bottom-width: 1px;\n"
            "    border-style: solid;\n"
            "    color: rgb(255, 255, 255);\n"
            "    padding: 2px;\n"
            "    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
            "}\n"
            "QPushButton:hover{\n"
            "    border-style: outset;\n"
            "    border-width: 2px;\n"
            "    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
            "    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
            "    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
            "    border-bottom-color: rgb(115, 115, 115);\n"
            "    border-bottom-width: 1px;\n"
            "    border-style: solid;\n"
            "    color: rgb(255, 255, 255);\n"
            "    padding: 2px;\n"
            "    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157, 255));\n"
            "}\n"
            "QPushButton:pressed{\n"
            "    border-style: outset;\n"
            "    border-width: 2px;\n"
            "    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(62, 62, 62, 255), stop:1 rgba(22, 22, 22, 255));\n"
            "    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
            "    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
            "    border-bottom-color: rgb(58, 58, 58);\n"
            "    border-bottom-width: 1px;\n"
            "    border-style: solid;\n"
            "    color: rgb(255, 255, 255);\n"
            "    padding: 2px;\n"
            "    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
            "}\n"
            "QPushButton:disabled{\n"
            "    border-style: outset;\n"
            "    border-width: 2px;\n"
            "    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
            "    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
            "    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
            "    border-bottom-color: rgb(58, 58, 58);\n"
            "    border-bottom-width: 1px;\n"
            "    border-style: solid;\n"
            "    color: rgb(0, 0, 0);\n"
            "    padding: 2px;\n"
            "    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(77, 77, 77, 255));\n"
            "}\n"
            "QLineEdit {\n"
            "    border-width: 1px; border-radius: 4px;\n"
            "    border-color: rgb(58, 58, 58);\n"
            "    border-style: inset;\n"
            "    padding: 0 8px;\n"
            "    color: rgb(255, 255, 255);\n"
            "    background:rgb(100, 100, 100);\n"
            "    selection-background-color: rgb(187, 187, 187);\n"
            "    selection-color: rgb(60, 63, 65);\n"
            "}\n"
            "QLabel {\n"
            "    color:rgb(255,255,255);    \n"
            "}\n"
            "QProgressBar {\n"
            "    text-align: center;\n"
            "    color: rgb(240, 240, 240);\n"
            "    border-width: 1px; \n"
            "    border-radius: 10px;\n"
            "    border-color: rgb(58, 58, 58);\n"
            "    border-style: inset;\n"
            "    background-color:rgb(77,77,77);\n"
            "}\n"
            "QProgressBar::chunk {\n"
            "    background-color: qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));\n"
            "    border-radius: 5px;\n"
            "}\n"
            "QMenuBar {\n"
            "    background:rgb(82, 82, 82);\n"
            "}\n"
            "QMenuBar::item {\n"
            "    color:rgb(223,219,210);\n"
            "    spacing: 3px;\n"
            "    padding: 1px 4px;\n"
            "    background: transparent;\n"
            "}\n"
            "\n"
            "QMenuBar::item:selected {\n"
            "    background:rgb(115, 115, 115);\n"
            "}\n"
            "QMenu::item:selected {\n"
            "    color:rgb(255,255,255);\n"
            "    border-width:2px;\n"
            "    border-style:solid;\n"
            "    padding-left:18px;\n"
            "    padding-right:8px;\n"
            "    padding-top:2px;\n"
            "    padding-bottom:3px;\n"
            "    background:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));\n"
            "    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
            "    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
            "    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
            "    border-bottom-color: rgb(58, 58, 58);\n"
            "    border-bottom-width: 1px;\n"
            "}\n"
            "QMenu::item {\n"
            "    color:rgb(223,219,210);\n"
            "    background-color:rgb(78,78,78);\n"
            "    padding-left:20px;\n"
            "    padding-top:4px;\n"
            "    padding-bottom:4px;\n"
            "    padding-right:10px;\n"
            "}\n"
            "QMenu{\n"
            "    background-color:rgb(78,78,78);\n"
            "}\n"
            "QTabWidget {\n"
            "    color:rgb(0,0,0);\n"
            "    background-color:rgb(247,246,246);\n"
            "}\n"
            "QTabWidget::pane {\n"
            "        border-color: rgb(77,77,77);\n"
            "        background-color:rgb(101,101,101);\n"
            "        border-style: solid;\n"
            "        border-width: 1px;\n"
            "        border-radius: 6px;\n"
            "}\n"
            "QTabBar::tab {\n"
            "    padding:2px;\n"
            "    color:rgb(250,250,250);\n"
            "      background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
            "    border-style: solid;\n"
            "    border-width: 2px;\n"
            "      border-top-right-radius:4px;\n"
            "   border-top-left-radius:4px;\n"
            "    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));\n"
            "    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));\n"
            "    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));\n"
            "    border-bottom-color: rgb(101,101,101);\n"
            "}\n"
            "QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
            "      background-color:rgb(101,101,101);\n"
            "      margin-left: 0px;\n"
            "      margin-right: 1px;\n"
            "}\n"
            "QTabBar::tab:!selected {\n"
            "        margin-top: 1px;\n"
            "        margin-right: 1px;\n"
            "}\n"
            "QCheckBox {\n"
            "    color:rgb(223,219,210);\n"
            "    padding: 2px;\n"
            "}\n"
            "QCheckBox:hover {\n"
            "    border-radius:4px;\n"
            "    border-style:solid;\n"
            "    padding-left: 1px;\n"
            "    padding-right: 1px;\n"
            "    padding-bottom: 1px;\n"
            "    padding-top: 1px;\n"
            "    border-width:1px;\n"
            "    border-color: rgb(87, 97, 106);\n"
            "    background-color:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 150), stop:1 rgba(93, 103, 113, 150));\n"
            "}\n"
            "QCheckBox::indicator:checked {\n"
            "    border-radius:4px;\n"
            "    border-style:solid;\n"
            "    border-width:1px;\n"
            "    border-color: rgb(180,180,180);\n"
            "      background-color:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));\n"
            "}\n"
            "QCheckBox::indicator:unchecked {\n"
            "    border-radius:4px;\n"
            "    border-style:solid;\n"
            "    border-width:1px;\n"
            "    border-color: rgb(87, 97, 106);\n"
            "      background-color:rgb(255,255,255);\n"
            "}\n"
            "QStatusBar {\n"
            "    color:rgb(240,240,240);\n"
            "}\n"
            "\n"
            "QPushButton{\n"
            "    border-style: solid;\n"
            "    border-color: #050a0e;\n"
            "    border-width: 1px;\n"
            "    border-radius: 5px;\n"
            "    color: #d3dae3;\n"
            "    padding: 2px;\n"
            "    background-color: #100E19;\n"
            "}\n"
            "QPushButton::default{\n"
            "    border-style: solid;\n"
            "    border-color: #050a0e;\n"
            "    border-width: 1px;\n"
            "    border-radius: 5px;\n"
            "    color: #FFFFFF;\n"
            "    padding: 2px;\n"
            "    background-color: #151a1e;\n"
            "}\n"
            "QPushButton:hover{\n"
            "    border-style: solid;\n"
            "    border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #C0DB50, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);\n"
            "    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #C0DB50, stop:1 #C0DB50);\n"
            "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
            "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
            "    border-width: 2px;\n"
            "    border-radius: 1px;\n"
            "    color: #d3dae3;\n"
            "    padding: 2px;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "    border-style: solid;\n"
            "    border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #d33af1, stop:0.4 #d33af1, stop:0.5 #100E19, stop:1 #100E19);\n"
            "    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #d33af1, stop:1 #d33af1);\n"
            "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
            "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
            "    border-width: 2px;\n"
            "    border-radius: 1px;\n"
            "    color: #d3dae3;\n"
            "    padding: 2px;\n"
            "}"
        )
        self.line = QtWidgets.QFrame(RegWindow)
        self.line.setGeometry(QtCore.QRect(0, 30, 521, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.min = QtWidgets.QPushButton(RegWindow)
        self.min.setGeometry(QtCore.QRect(520, 0, 41, 41))
        self.min.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.min.setText("")
        self.min.setObjectName("min")
        self.exit = QtWidgets.QPushButton(RegWindow)
        self.exit.setGeometry(QtCore.QRect(560, 0, 41, 41))
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit.setText("")
        self.exit.setObjectName("exit")
        self.label_name = QtWidgets.QLabel(RegWindow)
        self.label_name.setGeometry(QtCore.QRect(4, 0, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(16)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.lineEdit_email = QtWidgets.QLineEdit(RegWindow)
        self.lineEdit_email.setGeometry(QtCore.QRect(70, 310, 455, 34))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(13)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setInputMask("")
        self.lineEdit_email.setText("")
        self.lineEdit_email.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_email.setPlaceholderText("")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.label_enter = QtWidgets.QLabel(RegWindow)
        self.label_enter.setGeometry(QtCore.QRect(70, 200, 451, 111))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(20)
        self.label_enter.setFont(font)
        self.label_enter.setAlignment(QtCore.Qt.AlignCenter)
        self.label_enter.setObjectName("label_enter")
        self.lineEdit_password = QtWidgets.QLineEdit(RegWindow)
        self.lineEdit_password.setGeometry(QtCore.QRect(70, 370, 455, 34))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(13)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_password.setInputMask("")
        self.lineEdit_password.setText("")
        self.lineEdit_password.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_password.setPlaceholderText("")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.b_reg = QtWidgets.QPushButton(RegWindow)
        self.b_reg.setGeometry(QtCore.QRect(130, 440, 346, 37))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.b_reg.setFont(font)
        self.b_reg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_reg.setObjectName("b_reg")
        self.b_back = QtWidgets.QPushButton(RegWindow)
        self.b_back.setGeometry(QtCore.QRect(130, 480, 346, 37))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(14)
        self.b_back.setFont(font)
        self.b_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_back.setObjectName("b_back")

        self.retranslateUi(RegWindow)
        QtCore.QMetaObject.connectSlotsByName(RegWindow)

    def retranslateUi(self, RegWindow):
        _translate = QtCore.QCoreApplication.translate
        RegWindow.setWindowTitle(_translate("RegWindow", "Dialog"))
        self.lineEdit_email.setPlaceholderText("Логин")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setPlaceholderText("Пароль")
        self.label_name.setText(_translate("RegWindow", "Fitness system"))
        self.label_enter.setText(_translate("RegWindow", "Зарегистрируйтесь в системе"))
        self.b_reg.setText(_translate("RegWindow", "Зарегистрироваться"))
        self.b_back.setText(_translate("RegWindow", "Вернуться назад"))

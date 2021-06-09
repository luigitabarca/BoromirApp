

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import threading

class Ui_MainWindow():
    
    

    def __init__(self, MainWindow):
        self.MainWindow = MainWindow

        #widgets and spliter
        #self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.splitter_2 = QtWidgets.QSplitter(MainWindow)
        self.splitter_3 = QtWidgets.QSplitter(MainWindow)
        self.splitter_4 = QtWidgets.QSplitter(MainWindow)
        self.splitter = QtWidgets.QSplitter(MainWindow)
        #labels
        self.label_status = QtWidgets.QLabel(MainWindow)
        self.label_status_l = QtWidgets.QLabel(MainWindow)
        self.label_valoare = QtWidgets.QLabel(MainWindow)
        #butons
        self.pushButton_1 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_3 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_4 = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_6 = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_7 = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton_8 = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton_9 = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton_0 = QtWidgets.QPushButton(self.splitter_4)
        self.pushButton_point = QtWidgets.QPushButton(self.splitter_4)
        self.pushButton_Sterge = QtWidgets.QPushButton(self.splitter_4)
        self.pushButton_Enter = QtWidgets.QPushButton(MainWindow)
        self.pushButton_Porneste = QtWidgets.QPushButton(MainWindow)

        #texbox
        self.textEdit = QtWidgets.QTextEdit(MainWindow)

        #variable
        self.greutateIntrodusa=""


    def setupUi(self):

        #setup sliter property
        self.splitter.setGeometry(QtCore.QRect(10, 90, 421, 51))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setGeometry(QtCore.QRect(10, 150, 421, 51))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setGeometry(QtCore.QRect(10, 210, 421, 51))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setGeometry(QtCore.QRect(10, 270, 421, 51))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)

        #pozition butons
        self.pushButton_Porneste.setGeometry(QtCore.QRect(450, 150, 251, 101))
        self.pushButton_Porneste.setStyleSheet("background-color: rgb(255, 232, 117);")
        self.pushButton_Enter.setGeometry(QtCore.QRect(10, 330, 421, 51))
        #pozition labels
        self.label_status.setGeometry(QtCore.QRect(520, 100, 51, 21))
        self.label_valoare.setGeometry(QtCore.QRect(460, 30, 231, 41))
        self.label_status_l.setGeometry(QtCore.QRect(450, 100, 71, 21))
        #pozition texbox
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 421, 41))
        
        #set font
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_1.setFont(font)
        self.pushButton_2.setFont(font)
        self.pushButton_3.setFont(font)
        self.pushButton_4.setFont(font)
        self.pushButton_5.setFont(font)
        self.pushButton_6.setFont(font)
        self.pushButton_7.setFont(font)
        self.pushButton_8.setFont(font)
        self.pushButton_9.setFont(font)
        self.pushButton_0.setFont(font)
        self.pushButton_Sterge.setFont(font)
        self.pushButton_point.setFont(font)
        self.pushButton_Enter.setFont(font)
        #font buton pornire
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(60)
        self.pushButton_Porneste.setFont(font)

        #font label
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_status.setFont(font)
        self.label_status_l.setFont(font)
        self.label_valoare.setFont(font)

        #signals and event
        self.pushButton_0.clicked.connect(lambda: self.texboxenter(self.pushButton_0))
        self.pushButton_1.clicked.connect(lambda: self.texboxenter(self.pushButton_1))
        self.pushButton_2.clicked.connect(lambda: self.texboxenter(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda: self.texboxenter(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda: self.texboxenter(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.texboxenter(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.texboxenter(self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda: self.texboxenter(self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda: self.texboxenter(self.pushButton_8))
        self.pushButton_9.clicked.connect(lambda: self.texboxenter(self.pushButton_9))
        self.pushButton_point.clicked.connect(lambda: self.texboxenter(self.pushButton_point))
        self.pushButton_Sterge.clicked.connect(lambda: self.stergeText(self.pushButton_Sterge))
        self.pushButton_Enter.clicked.connect(lambda: self.valideazaGreutate())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_point.setText(_translate("MainWindow", "."))
        self.pushButton_Sterge.setText(_translate("MainWindow", "sterge"))
        self.pushButton_Enter.setText(_translate("MainWindow", "enter"))
        self.pushButton_Porneste.setText(_translate("MainWindow", "PORNESTE UMPLERE"))
        self.label_status_l.setText(_translate("MainWindow", "Status:"))
        self.label_status.setText(_translate("MainWindow", "Oprit"))
        self.label_valoare.setText(_translate("MainWindow", "Oprit"))

    def texboxenter(self,b):
        t=b.text()
        self.greutateIntrodusa=self.greutateIntrodusa + t
        self.textEdit.setText(self.greutateIntrodusa)

    def stergeText(self,b):
        self.greutateIntrodusa=self.greutateIntrodusa[:-1]
        self.textEdit.setText(self.greutateIntrodusa)

    def valideazaGreutate(self):
        self.label_valoare.setText(self.greutateIntrodusa)

    def afiseazaInTimpReal(self,text):
        self.label_status.setText(text)

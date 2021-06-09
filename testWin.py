
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from Ui_MainWindow import *
import threading
import serial
import sys







def main():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    
    ui=Ui_MainWindow(win)
    ui.setupUi()
    #ui.positionButton()
    ui.retranslateUi(win)
   
    win.show()
    sys.exit(app.exec_())

main()

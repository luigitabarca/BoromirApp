
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from Ui_MainWindow import *
import threading
import serial
import sys

serIndicator = serial.Serial("COM3",9600, timeout=1,parity=serial.PARITY_EVEN)

def handle_data(data,label_status):
    x=data[2:11].decode("ascii")
    label_status.setText(x)
 
def read_from_port(ser,label_status):
    while True:
        reading = ser.readline(22)
        handle_data(reading,label_status)

def on_button_clicked(label_status):
    thread = threading.Thread(target=read_from_port, args=(serIndicator,label_status,))
    thread.start()

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    
    ui=Ui_MainWindow(win)
    ui.setupUi()
    #ui.positionButton()
    ui.retranslateUi(win)
    ui.pushButton_Porneste.clicked.connect(lambda: on_button_clicked(ui.label_status))
    
    win.show()
    sys.exit(app.exec_())

main()

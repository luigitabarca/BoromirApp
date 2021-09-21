
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from Ui_MainWindow import *
import threading
import serial
import sys



#--for raspberry ony--
# import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
# GPIO.setup(19, GPIO.OUT)

# serIndicator = serial.Serial("COM3",9600, timeout=1,parity=serial.PARITY_EVEN)


def handle_data(data,label_status,label_valoare,thread):
    x=data[2:11].decode("ascii")
    real=float(x)
    # if label_status.text() == "Oprit":
    #     label_status.setText(x)
    introdus=float(label_valoare.text())
    if real>=introdus:
        label_status.setText("Oprit")
        # GPIO.output(19, 0) 
        
    else:
        label_status.setText(x)
 
def read_from_port(ser,label_status,label_valoare,thread):
    while True:
        reading = ser.readline(22)
        handle_data(reading,label_status,label_valoare,thread)


def on_button_clicked(label_status,label_valoare,pushButton_Porneste_2):
    thread = threading.Thread(target=read_from_port, args=(serIndicator,label_status,label_valoare,))
    thread.start()
    pushButton_Porneste_2.setText("Conectat")
    pushButton_Porneste_2.setStyleSheet("background-color:rgb(1, 170, 5);")
    pushButton_Porneste_2.setEnabled(False)

def on_button_clicked_1(ui):
    #thread.start()
    ui.quit()


#--for raspberry only--
def on_porneste_clicked(pin, ui, map):
    cell = ui.getSelectedCell()
    pinToStart = map[cell]
    print(pinToStart)
#     GPIO.output(pinToStart, 1)
   



def main():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    
    ui=Ui_MainWindow(win)
    ui.setupUi()
    #ui.positionButton()
    #thread = threading.Thread(target=read_from_port, args=(serIndicator,ui.label_status,ui.label_valoare,))

    ui.retranslateUi(win)

    # set cells to dropdown
    cellsToPinsMapping = {
        'celula1': 'PIN31',
        'celula2': 'PIN21',
        'celula3': 'PIN19',
        'celula4': 'PIN29'
    }
    ui.addItemToDropDown(cellsToPinsMapping.keys())

    
    # ui.pushButton_Porneste_2.clicked.connect(lambda: on_button_clicked(ui.label_status,ui.label_valoare,ui.pushButton_Porneste_2))
    ui.pushButton_Porneste_2.clicked.connect(lambda: on_button_clicked_1(app))
    pin=19
    ui.pushButton_Porneste.clicked.connect(lambda: on_porneste_clicked(pin, ui, cellsToPinsMapping))
    win.show()
    sys.exit(app.exec_())

main()

from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import threading
import serial
import sys
app = QApplication(sys.argv)
win = QMainWindow()
label = QLabel(win)

connected = False
serIndicator = serial.Serial("COM3",9600, timeout=1,parity=serial.PARITY_EVEN)





def handle_data(data):
    #print(data)
    x=data[2:11].decode("ascii")
    label.setText(x)
    #alert.exec()


def read_from_port(ser):
    # while not connected:
    #     #serin = ser.read()
    #     connected = True

    while True:
        print("test")
        reading = ser.readline(22)
        handle_data(reading)

def on_button_clicked():
    #alert = QLabel()
    # alert.setText('You clicked the button!')
    thread = threading.Thread(target=read_from_port, args=(serIndicator,))
    thread.start()
    # alert.exec()


def main():
    # app = QApplication(sys.argv)
    # win = QMainWindow()
    win.setGeometry(200,200,300,300) 
    win.setWindowTitle("My first window!") 
    
    #label = QLabel(win)
    label.setText("my first label")
    label.move(50, 50)  

    button = QtWidgets.QPushButton(win)
    button.setText("Start")
    button.clicked.connect(on_button_clicked)
    win.show()
    sys.exit(app.exec_())

main()


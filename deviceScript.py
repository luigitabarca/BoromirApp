import serial,time
import tkinter
import threading
import RPi.GPIO as GPIO
from datetime import datetime

 

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

 

serIndicator = serial.Serial("/dev/ttyUSB0",9600, timeout=1,parity=serial.PARITY_EVEN)
serPrint = serial.Serial("/dev/ttyUSB1", 9600, timeout=1)

 


def my_callback(channel): 
    serIndicator.close()
    serIndicator.open() 
    greutate=serIndicator.readline(22)
    print(greutate)
    serPrint.close()
    serPrint.open()
    greutate1=greutate[2:11]
    #antet
    antet=b'         Tichet   \n\n'
    
    antetGreutate=b'Greutatea este: '
    
    antetData=b'Data: '
    now=datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    n=bytes(dt_string, 'ASCII')
    space='\n\n\n\n\n'
    b = bytes(space, 'ASCII')
    serPrint.write(b)
    serPrint.write(antet)
    serPrint.write(antetGreutate)
    serPrint.write(greutate1)
    serPrint.write(b)
    serPrint.write(antetData)
    serPrint.write(n)
    serPrint.write(b)
    
    # //print ("falling edge detected on 17")
    
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback, bouncetime=1000)  

 


def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
    # stop listener; remove this if want more keys

 

listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main
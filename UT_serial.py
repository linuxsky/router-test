__author__ = 'shiyang'
#encoding:UTF-8

import serial
import time

def Test_serial_main(name,speed):
    ser = serial.Serial(name,speed,timeout=2)
    status = ser.isOpen()
    if (0 == status):
        print "Serial open failed!"
        return 1
    ser.write("\n")
    ser.write("ls\n")
    time.sleep(0.1)
    cnt = ser.inWaiting()
    str = ser.read(cnt)
    print str

    return 0
#!/usr/bin/python

import serial
import time

ser = serial.Serial('/dev/cu.KeySerial1', 9600, timeout=60)
logfile = open('test2.csv', 'a')
while True:
        line = ser.readline()
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        a =  "%s,%s" % (now,line)
        print a
        logfile.write(a)
        logfile.flush()
logfile.close()
ser.close()


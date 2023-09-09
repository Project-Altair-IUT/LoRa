import os
import serial



ser = serial.Serial(port = 'COM3' , baudrate=115200 , timeout=1)
while True:
    line = ser.readline().decode().strip()
    if len(line) >3:
        print(line)
        var = os.popen(line)
        ser.write(var.read().encode())
        print(var.read())

            

#!/usr/bin/env python
import time
import serial
import os
import subprocess
import json
import urllib.request
import shlex
from subprocess import Popen

counter= 0
pulse = 0.0
minpulse = 500
maxpulse = 2500

#def abrirserial():
#	try:
ser = serial.Serial(
port='/dev/ttyACM0',
baudrate = 115200,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1)
#	except serial.serialutil.SerialException:
#		print("Error al tratar de conectar al puerto serial, revisar conexion raspberry a placa servo")

def rangoservo(motor, angulo, tiempo=1000):
	rango = []
	rango.append([0, 70, 110])	#
	rango.append([1, 70, 110])	#
	rango.append([2, 70, 110])	#
	rango.append([3, 70, 110])	#
	rango.append([4, 20, 160])	# Giro cabeza 
	rango.append([5, 70, 110])	#
	rango.append([6, 70, 110])	#
	rango.append([7, 70, 110])	#
	rango.append([8, 70, 110])	#
	rango.append([9, 70, 110]) #
	rango.append([10, 70, 110]) #
	rango.append([11, 70, 110]) #
	rango.append([12, 70, 110]) #
	rango.append([13, 70, 110]) #
	rango.append([14, 70, 110]) #
	rango.append([15, 70, 110]) #
	rango.append([16, 70, 110]) #
	rango.append([17, 70, 110]) #
	rango.append([18, 70, 110]) #
	rango.append([19, 70, 110]) #
	rango.append([20, 70, 110]) #
	rango.append([21, 70, 110]) #
	rango.append([22, 70, 110]) #
	rango.append([23, 70, 110]) #

	for i in range(len(rango)):
#		print(rango[i])
		if (rango[i][0]==motor):
			if (rango[i][2] >= angulo >= rango[i][1]):
				return True
	return False

def servo(motor, angulo, tiempo=1000):
	pulse = (((maxpulse - minpulse)/180)*angulo)+510
	if (rangoservo(motor, angulo)):
		ser.write(('#%d P%d T%d \r' % (motor, pulse, tiempo)).encode())
#		print("Moviendo motor")
	else:
		print("fuera de rango")

#Ejemplo de cadena command = "\#(4 P1500 T1800 \r)"
def wolfram(question):
	command = "python3 wolfram.py \"" + question + " \""
	rspta=subprocess.check_output(command, shell=True)
	otro= rspta.decode('UTF-8')
#	escaped = otro.translate(str.maketrans({"-":  r"\-",
	#escaped = re.otro

	print(otro)
	return otro

def say(question):
#        command = "python3 saytts.py \"" + question + "\""
        command = "python3 saytts.py \"Viva el Peru carajo, hoy le ganamos a colombia 8 a 0 con goles de cubillas y cueto \""
        print(command)

        subprocess.Popen(command, shell=True)
#        print (rspta.decode('UTF-8'))
#	return rspta.decode('UTF-8')

def run_command(question):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
#    while True:
#    output = process.stdout.readline().decode('UTF-8')
#    print (output.strip())
#       if output == '' and process.poll() is not None:
#            break
#        if output:
#            print (output.strip())
#            print (output.strip())
#            print (output.strip())
#            print (output.strip())
#    rc = process.poll()
#    return rc

text = wolfram("who is the president of peru")
servo(4,90)
print(text)
#run_command("where i am")
say(text)
#print ("fin")
#if abrirserial():
servo(4,120)
time.sleep(1)
servo(6,70,200)
time.sleep(.2)
servo(6,100,200)
time.sleep(.2)
servo(6,70,200)
time.sleep(.2)
servo(6,100,200)
time.sleep(.2)
servo(6,70,200)
time.sleep(.2)
servo(6,70,200)
time.sleep(.2)
servo(6,100,200)
time.sleep(.2)
servo(6,70,200)
time.sleep(.2)
servo(6,100,200)
time.sleep(.2)
servo(6,70,200)
time.sleep(.2)
servo(6,100,200)
time.sleep(.2)
servo(6,70,200)
time.sleep(.2)
servo(6,100,200)
time.sleep(.2)
servo(6,70,200)
time.sleep(.2)
servo(6,70,200)
time.sleep(.2)
servo(6,100,200)
time.sleep(.2)
servo(6,70,200)
time.sleep(.2)
servo(6,100,200)
time.sleep(.2)
servo(6,70,200)
time.sleep(.2)
servo(6,100,200)
time.sleep(.2)
servo(6,70,200)
time.sleep(.2)
servo(6,100,200)
time.sleep(.2)
servo(6,70,200)
time.sleep(.2)
servo(6,100,200)
time.sleep(.2)
servo(6,70,200)
time.sleep(.2)
servo(6,100,200)
time.sleep(.2)
servo(6,70,200)
time.sleep(.2)
servo(6,70,200)
time.sleep(.2)
servo(6,100,200)
time.sleep(.2)
servo(6,70,200)
time.sleep(.2)
servo(6,100,200)
time.sleep(.2)
servo(6,70,200)
time.sleep(.2)

servo(4,90)

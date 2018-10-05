import RPi.GPIO as GPIO
from ./MFRC522/Read import Read
from client import Client
#from Solenoid import Solenoid (kalo udah ada)



reading = Read() #instansiasi class Read.py
client = Client() #instansiasi class lient.py

while True:
	if reading.detected(): #jika kartu terdeteksi
                client.open() # return activity ke webservice
		#solenoid.open() kalo udah ada
	
	else:
		client.lock()
		#solenoid.open() kalo udah ada


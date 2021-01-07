import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(21,GPIO.IN)


while True:
	time.sleep(2)
	iostate=GPIO.input(21)
	if iostate==False:
		print("water detected")
		GPIO.output(14,False)
		time.sleep(1)
	else:
		print("no water detected supply water")
		GPIO.output(14,True)
		time.sleep(1)

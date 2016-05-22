import RPi.GPIO as GPIO
import time
 
led_pin = 24
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
 
print "linker led pin 24 (BCM GPIO)"
 
while True:
	GPIO.output(led_pin,True)
	print "ON!"
	time.sleep(5)
	GPIO.output(led_pin,False)
	print "OFF!"
	time.sleep(5)
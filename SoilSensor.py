import RPi.GPIO as GPIO
import time

channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)

def callback(channel):
        if GPIO.input(channel):
                print("Water Detected!")
        else:
                print("No Water Detected!")

GPIO.add_event_detect(channel,GPIO.BOTH,bouncetime=300)
GPIO.add_event_callback(channel,callback)

try:
    while True:
        if GPIO.input(channel):
            print("Soil is wet")
        else:
            print("Soil is dry")
        time.sleep(10800)

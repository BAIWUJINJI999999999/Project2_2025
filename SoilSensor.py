import RPi.GPIO as GPIO
import PCF8591 as ADC
import time

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)
ADC.setup(0*48)

def callback(channel):
        if GPIO.input(channel):
                print("Water Detected!")
        else:
                print("No Water Detected!")

GPIO.add_event_detect(channel,GPIO.BOTH,bouncetime=300)
GPIO.add_event_callback(channel,callback)

try:
    while True:
        potentiometer_value = ADC.read(0)
        print(potentiometer_value)
        time.sleep(0.2)

except KeyboardInterrupt:
    print("Exit")

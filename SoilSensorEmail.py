import RPi.GPIO as GPIO
import time
import smtplib
from email.message import EmailMessage

channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)

from_email_addr="BAIWUJINJI999999@163.com"
from_email_pass="QGLmD7GAbyYEH8XJ"
to_email_addr="BAIWUJINJI999999@163.com"

last_send_time = 0

def callback(channel):

    if GPIO.input(channel): 
        print("Water Detected!")
    else:
        print("No Water Detected!")

GPIO.add_event_detect(channel,GPIO.BOTH,bouncetime = 300)
GPIO.add_event_callback(channel,callback)

def send_email(subject,body):
    global last_send_time
    current_time = time.time()

    if current_time - last_send_time >= 6*60*60:
        server = smtplib.SMTP('smtp.163.com', 25)
        server.starttls()
        server.login(from_email_addr,from_email_pass)

        msg = EmailMessage()
        msg.set_content(body)
        msg['From'] = from_email_addr
        msg['To'] = to_email_addr
        msg['Subject'] = subject

        server.send_message(msg)
        server.quit()
        print("Email Sent!")
        last_send_time = current_time

    else:
       print("Time interval not reached,email not sent")

def main():
    while True:
        current_time = time.localtime()
        current_hour = current_time.tm_hour 
        print("current time hour: ",current_hour)

        time.sleep(60*60)

        if current_hour % 6 == 0:
            current_value = GPIO.input(channel)
            status = "water detected"if current_value else "water not detected"
            subject = "soil sensor update"
            body =f"The soil sensor status is: {status}"
            send_email(subject,body)

if __name__== "__main__":
    main()

import RPi.GPIO as GPIO
import time
import smtplib
from email.message import EmailMessage

channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)

sensor_readings = []

def get_sensor_reading():
    return GPIO.input(channel)

def send_email_report(max_reading,min_reading):
    from_email_addr="BAIWUJINJI999999@163.com"
    from_email_pass="QGLmD7GAbyYEH8XJ"
    to_email_addr="BAIWUJINJI999999@163.com"

    msg = EmailMessage()
    body = f"Max Moisture Reading: {max_reading},Min Moisture Reading: {min_reading}"
    msg.set_content(body)
    msg['From'] = from_email_addr
    msg['To'] = to_email_addr
    msg['Subject'] = "Daily Moisture Report"

    server = smtplib.SMTP('smtp.163.com', 25)
    server.starttls()
    server.login(from_email_addr,from_email_pass)
    server.send_message(msg)
    server.quit()

for _ in range(8):
    reading = get_sensor_reading()
    sensor_readings.append(reading)
    time.sleep(10800)

max_reading = max(sensor_reading)
min_reading = min(sensor_reading)
send_email_report(max_reading,min_reading)

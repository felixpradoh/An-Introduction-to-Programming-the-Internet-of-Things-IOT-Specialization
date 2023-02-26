import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
# Set the pin configuration to board and the LED output pin to number 22
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.OUT)

pwm = GPIO.PWM(22,133) #Change the frequency to reduce interference with the camera at 50 Hz
pwm.start(0)

sleep_time = 0.1 # sleeps for 100 ms

# infinite loop for brighting and shadowing the LED
while True:
    for i in range(0,101):
        pwm.ChangeDutyCycle(i)
        time.sleep(sleep_time) 
    for i in range(100,0,-1):
        pwm.ChangeDutyCycle(i)
        time.sleep(sleep_time) 
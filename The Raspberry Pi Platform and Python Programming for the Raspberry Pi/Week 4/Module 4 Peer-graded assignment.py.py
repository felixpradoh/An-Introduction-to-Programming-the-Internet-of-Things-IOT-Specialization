import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
import time    # Import the sleep function from the time module

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BCM)     # Use physical pin numbering (BROADCOMM)

LED=18
TOGGLE=23
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(TOGGLE, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        
while True:
    try: 
        if GPIO.input(TOGGLE):
            GPIO.output(LED, GPIO.HIGH)      # Turn on
            time.sleep(0.5)                  # Sleep for 500 ms
            GPIO.output(LED, GPIO.LOW)       # Turn off
            time.sleep(0.5)                  # Sleep for 500 ms
        else:
            GPIO.output(LED, GPIO.HIGH)
            
    except KeyboardInterrupt:
        GPIO.cleanup()
        print('stopped!')
        exit()

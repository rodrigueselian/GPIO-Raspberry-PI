import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 18
RED = 27
GREEN = 17 

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()
    
    while GPIO.input(ECHO) == True:
        end = time.time()
    
    sig_time = end-start
    distance = sig_time / 0.000058
    print("distance: {} cm".format(distance))
    return distance

def close():
    GPIO.output(RED, GPIO.HIGH)
    GPIO.output(GREEN, GPIO.LOW)

def far():
    GPIO.output(RED, GPIO.LOW)
    GPIO.output(GREEN, GPIO.HIGH)

while True:
    distance = get_distance()
    time.sleep(0.1)
    if distance <= 5:
        close()
    else:
        far() 
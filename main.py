#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
import time
import subprocess

# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }

LedPin = 11    # pin11

def setup():
        GPIO.setmode(GPIO.BOARD)       # Set the board mode to numbers pins by physical location
        GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
        GPIO.output(LedPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the led

def loop():
        while True:
                out = subprocess.Popen(['sudo', 'examples/AdafruitDHT.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                stdout,stderr = out.communicate()
                if float(stdout.split()[0]) < 30:
                    GPIO.output(LedPin, GPIO.LOW)   # led on
                    time.sleep(1.0)                 # wait 1 sec
                else:
                    GPIO.output(LedPin, GPIO.HIGH)  # led off
                time.sleep(5.0)                 # wait 1 sec

def destroy():

        GPIO.output(LedPin, GPIO.HIGH)     # led off
        GPIO.cleanup()                     # Release resource


if __name__ == '__main__':     # Program start from here
        setup()
        try:
                loop()
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the destroy() will be  executed.
                destroy()

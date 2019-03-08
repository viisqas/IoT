#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
import time

import Adafruit_DHT


# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
#sensor 11 and pin 4
humidity, temperature = Adafruit_DHT.read_retry(11, 4)

# Un-comment the line below to convert the temperature to Fahrenheit.
# temperature = temperature * 9/5.0 + 32

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)


LedPin = 11    # pin11

def setup():
        GPIO.setmode(GPIO.BOARD)       # Set the board mode to numbers pins by physical location
        GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
        GPIO.output(LedPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the led

def loop():
        while True:
                humidity, temperature = Adafruit_DHT.read_retry(11, 4)
                if temperature < 30.0:
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

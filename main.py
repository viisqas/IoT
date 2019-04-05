#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
import time
import subprocess
import paho.mqtt.client as mqtt

LedPin = 11    # pin11

client = mqtt.Client()

client.connect("159.69.95.154", 1883, 60)

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

# The callback for when a PUBLISH message is received from the server.

def setup():
        GPIO.setmode(GPIO.BOARD)       # Set the board mode to numbers pins by physical location
        GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
        GPIO.output(LedPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the led

def loop():
        while True:
                out = subprocess.Popen(['sudo', 'examples/AdafruitDHT.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                stdout,stderr = out.communicate()
                temperature = float(stdout.split()[0])
                client.publish("house/temp", temperature)
                if temperature < 30.0:
                    print('Led on')
                    print('{0:0.1f}'.format(temperature))
                    GPIO.output(LedPin, GPIO.LOW)   # led on
                    time.sleep(1.0)                 # wait 1 sec
                else:
                    print('Led off')
                    print('{0:0.1f}'.format(temperature))
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

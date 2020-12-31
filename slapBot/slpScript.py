#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import socketio
import sys
import asyncio	

sio = socketio.Client()
motorPin = 7
GPIO.cleanup()

@sio.event
def connect():
    print('connection established')


@sio.on('event')
def event(data):
    print("received data from streamlabs:")
    print(data)


@sio.event
def disconnect():
    print('disconnected from server')
	#GPIO.cleanup()


def main():
	print("starting slapping bot!")
	print("GET READY")
	if(len(sys.argv) < 2 or sys.argv[1] is None):
		print("you must init this with an socketapi token")
		return
	initSocketio()
	initGpio()
	GPIO.output(motorPin, GPIO.HIGH)
	time.sleep(10)
	GPIO.output(motorPin, GPIO.LOW)



def initSocketio():
	print("setting up socket.io")
	global sio
	sio.connect("https://sockets.streamlabs.com?token=" + sys.argv[1], transports="websocket");
	#sio.wait()

def initGpio():
	print("setting up motor")
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(motorPin, GPIO.OUT)
	#GPIO.output(18, GPIO.HIGH)
	#GPIO.output(18, GPIO.LOW)


try:
    print("set GIOP high")


except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
	print("Keyboard interrupt")
	GPIO.cleanup()


except:
	print("some error") 

finally:
	print("clean up") 
	GPIO.cleanup() # cleanup all GPIO 


main()

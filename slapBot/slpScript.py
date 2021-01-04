#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import socketio
import sys
import json

sio = socketio.Client()
motorPin = 7
configuration = []

class Config:
	name = None
	value = 1
	on = False


@sio.event
def connect():
    print('connection established')


@sio.on('event')
def event(data):
	global configuration
	for cs in configuration:
		if(cs.name == data['type'] and cs.on):
			try:
				if(cs.value <= data['message'][0]['amount']):
					slap(len(data['message']))
			except:
				slap(len(data['message']))
	print("received data from streamlabs:")
	print(data)


@sio.event
def disconnect():
    print('disconnected from server')
	#GPIO.cleanup()


def main():
	print("starting slapping bot!")
	print("GET READY")
	loadConfig()
	if(len(sys.argv) != 2 or sys.argv[1] is None):
		print("you must init this with a socketapi token")
		return
	initSocketio()
	initGpio()


def slap(force = 1):
	GPIO.output(motorPin, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(motorPin, GPIO.LOW)


def initSocketio():
	print("setting up socket.io")
	global sio
	sio.connect("https://sockets.streamlabs.com?token=" + sys.argv[1], transports="websocket");

def initGpio():
	print("setting up motor")
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(motorPin, GPIO.OUT)

def loadConfig():
    fileContent = getConfigFileContent()
    global configuration	
    c = json.loads(fileContent)
    for conf in c:
        nConf = Config()
        nConf.name = conf['name']
        nConf.value = conf['value']
        nConf.on = conf['on']
        configuration.append(nConf)

def getConfigFileContent():
	f = None;
	try:
		f = open("/etc/slpConfig.json")
	except:
		f = open("./slapBot/slpConfig.json")
	return f.read()

try:
    print("preparing bot")


except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
	print("Keyboard interrupt")
	GPIO.cleanup()


main()

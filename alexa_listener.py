import logging
import os

from flask import Flask
from flask_ask import Ask, request, session, question, statement
import wiringpi

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

STATUSON = ['on','high']
STATUSOFF = ['off','low']
STATUSTOGGLE = ['toggle','flash','strobe']
STATUSCMD = ['a','be','see']

@ask.launch
def launch():
	speech_text = 'Welcome to Raspberry Pi Automation.'
	return question(speech_text).reprompt(speech_text).simple_card(speech_text)

@ask.intent('GpioIntent', mapping = {'status':'status'})
def Gpio_Intent(status,room):
	wiringpi.wiringPiSetupGpio ()
	
	wiringpi.pinMode(18, 2) # pwm mode = 2
	wiringpi.pwmSetMode(0)
	
	# pwmFrequency in Hz = 19.2e6 Hz / pwmClock / pwmRange.
	wiringpi.pwmSetRange(4096)
	wiringpi.pwmSetClock(4095)
	if status in STATUSON:
		wiringpi.pwmWrite(18, 4096)
		return statement('turning {} blue L E D'.format(status))
	elif status in STATUSOFF:
		wiringpi.pwmWrite(18, 0)
		return statement('turning {} blue L E D'.format(status))
	elif status in STATUSTOGGLE:
		wiringpi.pwmWrite(18, 2048)
		return statement('{}ing blue L E D'.format(status))
	elif status in STATUSCMD:
		serial = wiringpi.serialOpen('/dev/ttyAMA0',9600)
		if status == 'a':
			wiringpi.serialPuts(serial, 'a')
		elif status == 'be':
			wiringpi.serialPuts(serial, 'b')
		elif status == 'see':
			wiringpi.serialPuts(serial, 'c')
		wiringpi.serialClose(serial)
		return statement('Trying to send command ASCII character {}'.format(status))
	else:
		return statement('Sorry not possible.')

@ask.intent('AMAZON.HelpIntent')
def help():
	speech_text = 'You can say, "Turn L E D on", or, "Turn L E D off".'
	return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)


@ask.session_ended
def session_ended():
	return "{}", 200


if __name__ == '__main__':
	if 'ASK_VERIFY_REQUESTS' in os.environ:
		verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
		if verify == 'false':
			app.config['ASK_VERIFY_REQUESTS'] = False
	app.run(debug=True)

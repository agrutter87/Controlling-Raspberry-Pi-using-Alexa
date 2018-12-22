import logging
import os

from flask import Flask
from flask_ask import Ask, request, session, question, statement
import RPi.GPIO as GPIO

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

STATUSON = ['on','high']
STATUSOFF = ['off','low']
STATUSTOGGLE = ['toggle','flash','strobe']

@ask.launch
def launch():
    speech_text = 'Welcome to Raspberry Pi Automation.'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

@ask.intent('GpioIntent', mapping = {'status':'status'})
def Gpio_Intent(status,room):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)    
    GPIO.setup(18,GPIO.OUT)
    if status in STATUSON:
        GPIO.output(18, GPIO.HIGH)
        return statement('turning {} blue L E D'.format(status))
    elif status in STATUSOFF:
        GPIO.output(18, GPIO.LOW)
        return statement('turning {} blue L E D'.format(status))
    elif status in STATUSTOGGLE:
        return statement('{} command not yet supported'.format(status))
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

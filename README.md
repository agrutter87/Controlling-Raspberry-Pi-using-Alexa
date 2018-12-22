# Controlling-Raspberry-Pi-using-Alexa

My notes:

I really enjoyed the example project provided by nishit-patel. Check out his github and hackster.io projects!
I decided to fork this because I want to control some other stuff with it, and I like to track changes. 

I received my first Alexa Echo Dot as a dirty santa gift at work. Stole it from the owner! haha! It's cool he had a few already, so they were excited for me to have a new toy.
I was so impressed with the Dot's ability to hear and comprehend my voice across the 1-br apartment that I decided I wanted to be able to call it closer in the morning while I'm in the shower.
I've made a few small rovers now, and I think it would be pretty cool to use this demo as a starting point for a smart rover which would do some RPi camera/OpenCV based navigation to find its way to the bathroom with the Dot attached.


Original author notes:

Being able to control Raspberry Pi via voice commands is always amazing. I have demonstrated how you can control your Raspberry Pi using Amazon Alexa. For establishing connection between Raspberry Pi and Alexa, we are going to use certain open-source services and sdk. Logic for controlling Alexa commands and Raspberry Pi will be hosted on local server on Raspberry Pi. As you will require SSL certificates for 'endpoint' in Amazon Alexa, you can use certain open source services to establish tunneling from your Raspberry Pi to Amazon Alexa.

The skill for Alexa will be made using Flask-Ask. For establishing connection we will be using ngrok. ngrok establishes a HTTP tunnel from Raspberry Pi to Alexa. The endpoint url will change every time ngrok is restarted, as an alternative you can use pagekite.

For detailed information visit https://www.hackster.io/nishit-patel/controlling-raspberry-pi-using-alexa-33715b.

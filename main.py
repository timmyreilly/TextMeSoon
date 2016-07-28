#Main file
from datetime import datetime
import re
import time 

import Adafruit_CharLCD as LCD

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

from tokens import *
from twilio.rest import TwilioRestClient

def validNumber(phone_number):
    pattern = re.compile("(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", re.IGNORECASE)
    return pattern.match(phone_number) is not None

account = ACCOUNT_SID
token = AUTH_TOKEN
client = TwilioRestClient(account, token)

run = True; 

lcd.clear() 

while run == True:
    lcd.message("Phone number?: ")
    input = raw_input("What is your phone number?: ")
    if input == "q":
        run = False; 
        continue; 
    elif validNumber(input):
        print "You will receive a text when the coffee is ready"
        #time.sleep(10)
        lcd.message("We'll text when ready")
        message = client.messages.create(to=input, from_=TWILIO_NUMBER, body="Coffee is ready - " + "{:%Y-%m-%d %H:%M:%S}".format(datetime.now()))
        print message.sid
    else: 
        print "Invalid Number please try again"
        lcd.message("Try Again")
        time.sleep(0.5)

lcd.clear()






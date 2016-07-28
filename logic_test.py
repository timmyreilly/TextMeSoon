#Main file
from datetime import datetime
import re

import Adafruit_CharLCD as LCD

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

def validNumber(phone_number):
    pattern = re.compile("(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", re.IGNORECASE)
    return pattern.match(phone_number) is not None


lcd.clear()

run = True; 

while run == True:
    lcd.message("What is your phone number?: ")
    input = ""
    while validNumber(input) != True or len(input) > 11:
        input = raw_input("Next number: ")
        lcd.clear()
        lcd.message(input)

    if input == "q":
        run = False; 
        continue; 
    elif validNumber(input):
        print "You will receive a text when the coffee is ready"
        #time.sleep(10)
        #message = client.messages.create(to=input, from_=TWILIO_NUMBER, body="Coffee is ready - " + "{:%Y-%m-%d %H:%M:%S}".format(datetime.now()))
        #print message.sid
    else: 
        print "Please enter a valid phone number"

lcd.clear()     




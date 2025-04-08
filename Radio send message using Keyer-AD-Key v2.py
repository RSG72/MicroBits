from microbit import * 
import radio					#import radio library

radio.config(group=72, power=7) #use radio group 72; signal strength 0-7
radio.on() 

while True:
    message = radio.receive()
    if message:
        display.scroll(message,wait=False)	#wait=False means the programme will continue to run and not wait for the whole string to be displayed
    sleep(150)
    reading = pin1.read_analog()			#takes analog reading from Pin 1 (Note: Pin 0 can have an issue with music)
    print("Reading: " + str(reading))		#display reading to shell
    if reading <20:							#SW1 - left is pressed
        radio.send('left')
    elif reading <160:						#SW2 - up is pressed
        radio.send('up')
    elif reading <350:						#SW3 - down is pressed
        radio.send('down')
    elif reading <520:						#SW4 - right is pressed
        radio.send('right')
    elif reading > 730 and reading <750:	#SW5 - "fire" is pressed
        radio.send('fire')
  

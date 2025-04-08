from microbit import * 
import radio								#import radio library

radio.config(group=72, power=7) 			#use radio group 72; signal strength 0-7
radio.on() 

while True:
    if button_a.was_pressed():
        radio.send('hello')
    elif button_b.was_pressed():
        radio.send('goodbye')
    message = radio.receive()
    if message:
        display.scroll(message,wait=False)	#wait=False means the programme will continue to run and not wait for the whole string to be displayed
from microbit import *
import music

def left(): 	#will move the pixel left 1
    global x
    x-=1
    if x==-1:	#if pixel goes off the display to the left
        x=4		#show pixel on the right
    
def right():	#will move the pixel right 1
    global x
    x+=1
    if x==5:	#if pixel goes off the display to the right
        x=0		#show pixel on the left
    
def up():		#will move the pixel up 1
    global y
    y-=1
    if y==-1:	#if pixel goes off the display at the top
        y=4		#show pixel on the bottom

    
def down():		#will move the pixel down 1
    global y
    y+=1
    if y==5:	#if pixel goes off the display at the bottom
        y=0		#show pixel on the top
    
def fire():
    music.play('a')
    music.stop()
    
#main programme    
x=2							#set the pixel in the horizonal middle
y=2							#set the pixel in the vertical middle
display.clear()	
display.set_pixel(x,y,4)	#displays with a brightness of 4
while True: 				#main loop
    sleep(100)
    reading = pin1.read_analog()	#takes analog reading from Pin 1 (Note: Pin 0 can have an issue with music)
    print("Reading: " + str(reading)) #display reading to shell
    if reading <20:			#SW1 - left is pressed
        left()
    elif reading <160:		#SW2 - up is pressed
        up()
    elif reading <350:		#SW3 - down is pressed
        down()
    elif reading <520:		#SW4 - right is pressed
        right()
    elif reading > 730 and reading <750:	#SW5 - "fire" is pressed
        fire()
    display.clear()
    display.set_pixel(x,y,4)


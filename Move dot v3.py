from microbit import *
import music, random, time	#time library to allow game play time to be calculated

def left():		#will move the pixel left 1
    global x
    x-=1
    if x==-1:	#if the pixel goes off the left of the display
        x=4		# bring the pixel back on the right
    
def right():	#will move the pixel right 1
    global x
    x+=1
    if x==5:	#if the pixel goes off the right of the display
        x=0		# bring the pixel back on the left
    
def up():		#will move the pixel up 1
    global y
    y-=1
    if y==-1:	#if the pixel goes off the top of the display
        y=4		# bring the pixel back at the bottom

def down():		#will move the pixel down 1
    global y
    y+=1
    if y==5:	#if the pixel goes off the bottom of the display
        y=0		# bring the pixel back at the top
    
def fire():		#still not utilised in this game
    music.play('a')
    sleep(100)
    music.stop()

x=2				#sets the pixel in the middle horizontally
y=2				#sets the pixel in the middle vertically
count=0			#initiates the counter to 0
start = running_time()	#sets the start time as now
tx=random.randint(0, 4)	#sets the target pixel random horizontally
ty=random.randint(0, 4)	#sets the target pixel random vertically
display.clear()
display.set_pixel(tx,ty,9)	#displays the target pixel - full brightness
sleep(500)
display.set_pixel(x,y,6)	#displays the moveable pixel - not as bright
while count<5: 				#loops the game 5 times
    sleep(150)
    reading = pin1.read_analog()		#takes analog reading from Pin 1 (Note: Pin 0 can have an issue with music)
    print("Reading: " + str(reading))	#display reading to shell
    if reading <20:			#SW1 - left is pressed
        left()
    elif reading <160:		#SW2 - up is pressed
        up()
    elif reading <350:		#SW3 - down is pressed
        down()
    elif reading <520:		#SW4 - right is pressed
        right()
    elif reading > 730 and reading <750:	#SW5 - "fire" is pressed (still not utilised in this game)
        fire()
    display.clear()				#refresh the display
    display.set_pixel(tx,ty,9)	#refresh the display
    display.set_pixel(x,y,4)	#refresh the display
    if x==tx and y==ty:			#if the target has been reached
        music.play(music.POWER_UP, wait=False)	#play success sound - the wait=false means the next lines of code are run immediately rather than waiting for the music to finish
        for i in range(8):		#flashes the hit target explosion 8 times
            display.show(Image('50005:'
                   '05050:'
                   '00500:'
                   '05050:'
                   '50005'))
            sleep(50)
            display.show(Image('00000:'
                   '09090:'
                   '00900:'
                   '09090:'
                   '00000'))
            sleep(50)
        count+=1				#increases the target hit counter
        display.clear()
        tx=random.randint(0, 4)	#generate a new horizontal location for the target 
        while tx==x:			#re-generates horizonal location if our moveable pixel is already there
            tx=random.randint(0, 4)
        ty=random.randint(0, 4)	#generate a new vertical location for the target
        while ty==y:			#re-generates vertical location if our moveable pixel is already there
            ty=random.randint(0, 4)
        display.set_pixel(tx,ty,9)
        display.set_pixel(x,y,4)
        print("Count: " + str(count))
end = running_time()			#after 5 games sets the finish time as now
howlong=end-start				#calculates the duration of the game
display.scroll(howlong/1000, delay=150)	#displays the time twice
display.scroll(howlong/1000, delay=150)	

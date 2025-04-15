# Simon Game for Micro:Bit
#Using 5 button Keyes Keyer-AD-Key K845037
#adapted from www.101computing.net/microbit-simon-game

from microbit import *
import random, music

left = Image("00000:"
             "50000:"
             "95000:"
             "50000:"
             "00000")
             
right = Image("00000:"
             "00005:"
             "00059:"
             "00005:"
             "00000")

up = Image("05950:"
             "00500:"
             "00000:"
             "00000:"
             "00000")

down = Image("00000:"
             "00000:"
             "00000:"
             "00500:"
             "05950")

def fire():		#not utilised in this game; NOTE: SW5 is used to restart the game 
    music.pitch(0,0) #0 frequency 0 milliseconds
    sleep(0)
    music.stop()

OPTIONS = ["L", "R", "U", "D"] #left, right, up, down

hi_score=0
music.play(music.POWER_UP, wait=True)	#play a "let's play" tune
sleep(500)
restart=True	#allows the game to start the first time
while restart == True: #master game loop that allows the game to be restarted with SW5 button after the end of a game
    sequence = random.choice(OPTIONS)  #Puts first random Up, Down, Left, Right in the sequence   
    correct = True		#the game can start in the first pass and continue thereafter until a mistake is made
    while correct == True:
        for character in sequence:	#Repeats for as long as there are L,R,U,D characters in the sequence
            if character=="L":
                display.show(left)
                music.pitch(589)
            elif character=="R":
                display.show(right)
                music.pitch(494)
            elif character=="U":
                display.show(up)
                music.pitch(440)
            elif character=="D":
                display.show(down)
                music.pitch(523)
            sleep(500)
            music.stop()
            display.clear()
            sleep(250)
        display.show("?")
        sleep(500)
        display.clear()
        maxInputs = len(sequence) #how long is the current sequence?
        capturedInputs = 0        #resets the counter of the user's responses as you work through the sequence 
        while capturedInputs < maxInputs and correct == True: #keeps looping provided no errors in the user responses and there are still letters left in the sequence
            reading = pin1.read_analog()		#takes analog reading from Pin 1 (Note: Pin 0 can have an issue with music)
            if reading <20:			#SW1 - left is pressed
                display.show(left)
                music.pitch(589)
                if sequence[capturedInputs] == "L": #if the user response was correct
                    correct = True					#keep going
                else: 
                    correct = False					#oops; user got it wrong - we'll stop  :o(
                capturedInputs += 1                 #increments to the next location in the sequence
            elif reading <160:		#SW2 - up is pressed
                display.show(up)
                music.pitch(440)
                if sequence[capturedInputs] == "U":
                    correct = True
                else: 
                    correct = False
                capturedInputs += 1
            elif reading <350:		#SW3 - down is pressed
                display.show(down)
                music.pitch(523)
                if sequence[capturedInputs] == "D":
                    correct = True
                else: 
                    correct = False
                capturedInputs += 1
            elif reading <520:		#SW4 - right is pressed
                display.show(right)
                music.pitch(494)
                if sequence[capturedInputs] == "R":
                    correct = True
                else: 
                    correct = False
                capturedInputs += 1
            elif reading > 730 and reading <750:	#SW5 - "fire" is pressed (currently does nothing - but will be used to reset the game)
               fire() 
            sleep(500)
            music.stop()
            display.clear()
        if correct==True:	#well done player you got the sequence correct
            sequence = sequence + random.choice(OPTIONS) #makes the sequence one random option longer
            display.show(Image.HAPPY)
            sleep(800)
            display.clear()
    sleep(200)
    music.play(music.FUNERAL,wait=False)
    display.scroll("Game Over", delay=75)  #Display Game Over #
    if len(sequence) > hi_score:
        hi_score=len(sequence)
    display.scroll("Score " + str(len(sequence)), delay=75) #show the final score
    restart=False	#a boolean flag to keep repeating the score until a player hits SW5 to restart the game
    while restart==False:	#repeats the score until we restart
        reading = pin1.read_analog()		#takes analog reading from Pin 1 (Note: Pin 0 can have an issue with music)
        if reading > 730 and reading <750:	#SW5 let's play again!!
            restart=True
            music.play(music.POWER_UP, wait=True)	#play a "let's play" tune
            sleep(1000)
        else:								#keep repeating the score
            display.scroll(str(len(sequence)), delay=100)
        if button_a.was_pressed():
            display.scroll("High Score " + str(hi_score), delay=75) #show the high score
            display.scroll(str(hi_score), delay=75) #show the high score
            display.scroll("Last Score ", delay=75)
            
 


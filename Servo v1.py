from microbit import * 
# Servo control: 
# 50 = ~1 millisecond pulse all right 
# 75 = ~1.5 millisecond pulse center - Stop 
# 100 = ~2.0 millisecond pulse all left 
pin2.set_analog_period(20)

while True: 
    display.show(Image.NO) 		#stop turning
    pin2.write_analog(75)    
    sleep(1000)
    display.show(Image.ARROW_E) #right clockwise
    pin2.write_analog(50)
    sleep(1000)
    display.show(Image.NO)		#stop turning 
    pin2.write_analog(75)
    sleep(1000)
    display.show(Image.ARROW_W)  #left anitclockwise
    pin2.write_analog(100)
    sleep(1000)
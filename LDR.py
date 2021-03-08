import pyfirmata2
from pyfirmata2 import Arduino, util
import time

board = Arduino('COM4')

it = util.Iterator(board)
it.start()

light = board.get_pin('a:0:i')
led = board.get_pin('d:13:o')

while True:

    brightness = light.read()
    
    if brightness == None:
        #when data variable first assigned, type is none
        continue
    else:
        brightness = (brightness*1000)
        print(brightness)
        if brightness<900:
            led.write(0)
        else:
            led.write(1)
             
    time.sleep(1)


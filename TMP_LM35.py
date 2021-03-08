import pyfirmata2
from pyfirmata2 import Arduino, util
import time


board = Arduino('COM4')

it = util.Iterator(board)
it.start()

analogZero = board.get_pin('a:0:i')
led = board.get_pin('d:13:o')

while True:

    reading = analogZero.read()
    
    
    
    if reading == None:
        #when data variable first assigned, type is none
        continue
    else:
        voltage = reading*5000
        voltageAtBitLevel = (voltage/1024)*100
        temperature = (voltageAtBitLevel-0.5)
        print(temperature)
        if temperature>29:
            led.write(1)
        else:
            led.write(0)
             
    time.sleep(1)


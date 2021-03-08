import pyfirmata2
from pyfirmata2 import Arduino, util
import time

board = Arduino('COM4')

it = util.Iterator(board)
it.start()

pir = board.get_pin('d:2:i')
led = board.get_pin('d:13:o')


while True:

    pirVal = pir.read()
    #print(pirVal)
    if pirVal == None:
        #when data variable first assigned, type is none
        continue
    else:
        
        if pirVal==1:
            startTime=time.time()
            led.write(0)
            
        else:
            led.write(1)
            endTime=time.time()
            tmer=startTime-endTime
            #print(tmer)
             
    #time.sleep(1)


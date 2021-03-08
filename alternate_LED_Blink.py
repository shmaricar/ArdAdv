from pyfirmata2 import Arduino, util
import time
board = Arduino('COM4')

while True:
    board.digital[13].write(1)
    board.digital[12].write(0)
    time.sleep(1)
    board.digital[13].write(0)
    board.digital[12].write(1)
    time.sleep(1)

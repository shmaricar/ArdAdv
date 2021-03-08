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
    print(type(brightness))
    time.sleep(1)


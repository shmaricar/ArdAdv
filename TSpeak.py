from pyfirmata2 import Arduino, util
from urllib.request import urlopen
import time 
board = Arduino('COM4')
it = util.Iterator(board)
it.start()

myAPI = 'SZ85C9HKR071NEG2' 
#for getting the myAPI key value, refer to the pdf tutorial, Setting up a ThingSpeak Account and creating and saving a channel with write API Key
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 
temperature = board.get_pin('a:0:i')
while True:
    t = temperature.read()
    if t == None:
        continue
    else:
        temp = (t*1000)/1.9
        temp = '%.2f' % temp
        conn = urlopen(baseURL + '&field1=%s' % temp)
    print(temp)    
    time.sleep(1)

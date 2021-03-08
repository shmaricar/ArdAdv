from pyfirmata2 import Arduino, util
import smtplib,ssl
import time
import os

board = Arduino('COM4')
it = util.Iterator(board)
it.start()
analogZero = board.get_pin('a:0:i')
led = board.get_pin('d:13:o')

def send_email():
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "shmaricar@gmail.com"
    receiver_email = "shmaricar@gmail.com"
    # you can replace the above line of code with receiver_email = os.environ.get('EMAIL_ADDRESS') if you dont wish to 
    #use your own email address in this code
    #refer to the pdf tutorial 'Generate a password for triggering an email alert and inputting email and password into the Environment Variable'
    password = os.environ.get('EMAIL_PASSWORD')
    #for generating the email password to be used with the line of code directly above using the
    #os.enviro.get method, refer to the pdf tutorial 'Generate a password for triggering an email alert and inputting email and password into the Environment Variable'
    subject='Temperature Rise Alert'
    body='Temperature of system rose above 29 degrees.'
    message = f'Subject: {subject}\n\n{body}'
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message, subject)
        print("message sent")
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
            send_email()
        else:
            led.write(0)
             
    time.sleep(1)

import serial
ArdData = serial.Serial('COM4', 9600)

while True:
    print("The distance of the object is:")
    x=ArdData.readline()
    print(str(x.decode().strip()))
    #remove b(bytes) prefix with .decode and carriage return/new line with .strip()



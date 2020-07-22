import time

#need to install pyserial before you can use this module
#which can be done by typing:
#  pip install pyserial
#into the terminal as long as you have python installed first
import serial



#arch linux
#programLocation = "/usr/bin/arduino"

arduinoPort = "COM14"


def SERIAL_TO_TEXT():

    # you can also google how to create a serial object to use for this script
    # but this is initializing a object with the serial.Serial functions
    s = serial.Serial()

    # we are setting up the serial.Serial.port setting
    # you can also just put the string "COM14" to the right of the equal sign instead of arduinoPort
    s.port = arduinoPort

    # the baud rate has to match what is set on the microcontroller
    s.baudrate = 9600

    # This is how many seconds before the serial port on the PC side waits before assuming no data from the microcontroller
    s.timeout = 5

    s.open()
    # print("opening serial line")

    # toggling these lines to reset the arduino
    # this doesn't need to be done, but this will make sure arduino
    # is starting from the beginning of it's code.
    s.setDTR(False)
    s.setRTS(False)
    time.sleep(.2)
    s.setDTR(True)
    s.setRTS(True)

    # print statements can be used in python as debug points to make sure that
    # the code arrived at this point.
    print("Serial port setup complete")

    try:
        #initializing arduino string to be empty
        arduinoSerial = ""

        #initialize a file object to write to when we receive data
        serialRecord = open("Testing_serial", "a")

        print("Starting to read from serial port")
        while(True):

            if(s.in_waiting > 0):
                # the readline function reads from the serial port and outputs
                # the byte datatype, not a string
                arduinoSerial = s.readline()
                # we can still print out a byte by itself
                print(arduinoSerial)

                # if we want to concatinate a string to the output we need to convert
                # the byte to a string using str()
                print("This is the output from the serial line:" + str(arduinoSerial))

                # if we want to record the data to a text file we need to convert it
                serialRecord.write(str(arduinoSerial))


    except KeyboardInterrupt:
        print("\nexistential crisis") #why not
        s.close()



# if __name__ == "__main__":
#     SERIAL_TO_TEXT()

SERIAL_TO_TEXT()

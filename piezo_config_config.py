import serial

import time



def read_from_serial(serial_port, timeout=2):

    start_time = time.time()

    while True:

        # Read a line from the serial port

        line = serial_port.readline().decode('utf8').strip()

        

        if line:

            # Print the received line if not empty

            print(line)

        else:

            # Check if the timeout period has elapsed

            if time.time() - start_time > timeout:

                print("Timeout reached, no more data.")

                break

            # Otherwise, wait a bit before the next read

            time.sleep(0.1)



# Open serial port with a timeout of 1 second (adjusted as needed)

ser = serial.Serial('/dev/serial0', 9600, timeout=1)

ser.flush()



# Read user input

user_message = input("Enter the message to send: ")



# Write user input to UART with a space before the newline

ser.write((user_message + ' \n').encode())



# Allow some time for the response

time.sleep(1)



# Read text from UART with a 2-second timeout

read_from_serial(ser, timeout=2)



# Close the serial port

ser.close()


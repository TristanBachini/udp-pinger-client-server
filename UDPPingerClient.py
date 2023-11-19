from socket import *
import time
from datetime import datetime
def main():
    # Create a UDP socket
    # Notice the use of SOCK_DGRAM for UDP packets
    for i in range(10):
        print(f"Ping number: {i+1}")
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        #create the message
        message = 'The time is {}'.format(time.time())
        message = message.encode('ascii')
        # Receive the server packet along with the address it is coming from
        start_time = time.time()
        clientSocket.sendto(message, ('127.0.0.1',12000))
        clientSocket.settimeout(1.0)
        try:
            message, address = clientSocket.recvfrom(1024)
            # Display the sender and the message received
            print(f'RTT: {time.time()-start_time}')
            # Capitalize the message from the client
            message = message.upper()
            time.sleep(.05) # DEBUG1: Wait only to simulate longer delay and test timeout large = more likely for timeout
        except timeout:
            print("packet has been lost.")


if __name__ == '__main__':
    main()
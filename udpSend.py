import socket
import datetime
import sys
import time

receiveIP = "10.10.10.10"
udpPort = 5005
bufferSize = 1024
udpAddress = (receiveIP, udpPort)

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

print("Sending to ",receiveIP, " port ", udpAddress)
print("Ctrl-C to terminate")
# Send to server using created UDP socket
while (True):
    try:
        curTime = datetime.datetime.now()
        msg ="sending time:" + curTime.strftime("%m/%d/%Y, %H:%M:%S.%f")
        bytesToSend = str.encode(msg)
        print("msg: ", msg)
        UDPClientSocket.sendto(bytesToSend, udpAddress)
        time.sleep(0.75)
    except KeyboardInterrupt:
        print("keyboard interrupt! exiting")
        sys.exit()

import socket
import sys

receiveIP = "10.10.10.10"
udpPort = 5005
bufferSize = 1024
udpAddress = (receiveIP,udpPort)

#msgFromServer = "Hello UDP Client"
#bytesToSend = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind(udpAddress)

print("UDP server up and listening", udpAddress )

# Listen for incoming datagrams
while (True):
    try:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        print(f"Message from Client({address}):{message}")

    except KeyboardInterrupt:
        print("keyboard interrupt! exiting")
        sys.exit()


import socket
import sys

receiveIP = "10.10.10.10"
udpPort = 5005
bufferSize = 1024

#msgFromServer = "Hello UDP Client"
#bytesToSend = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((receiveIP, udpPort))

print("UDP server up and listening")

# Listen for incoming datagrams
while (True):
    try:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]

        clientMsg = "Message from Client:{}".format(message)
        clientIP = "Client IP Address:{}".format(address)

        print(clientMsg)
        print(clientIP)
    except KeyboardInterrupt:
        print("keyboard interrupt! exiting")
        sys.exit()

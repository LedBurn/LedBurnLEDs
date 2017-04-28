import socket

# A UDP server

# Set up a UDP server
UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDPSock2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Listen on port 5005
# (to all IP addresses on this system)
listen_addr = ("",5005)
# listen_addr2 = ("",5006)
UDPSock.bind(listen_addr)
# UDPSock2.bind(listen_addr2)

# Report on all data packets received and
# where they came from in each case (as this is
# UDP, each may be from a different source and it's
# up to the server to sort this out!)
while True:
        data,addr = UDPSock.recvfrom(1024)
        print data.strip(),addr
        # data,addr = UDPSock2.recvfrom(1024)
        # print data.strip(),addr
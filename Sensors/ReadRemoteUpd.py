
import socket

def create_udp_listen_sock(port):
    udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    listen_addr = ("", port)
    udpSock.bind(listen_addr)
    udpSock.setblocking(0)
    return udpSock

def read_non_blocking_udp(UDPSock):
	try:
		data, addr = UDPSock.recvfrom(1024)
		#print data.strip(), addr
		return float(data.strip())
	except:
		return None





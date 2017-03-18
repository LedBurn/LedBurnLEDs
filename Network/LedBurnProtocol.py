
import socket
import array

CONTROLER_IP = "10.0.0.210"
UDP_PORT = 2000

sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

def uint8_to_array(num):
    c1 = (num / (1)) % 256
    return [c1]

def uint16_to_array(num):
    c1 = (num / (256)) % 256
    c2 = (num / (1)) % 256
    return [c2, c1]

def uint32_to_array(num):
    c1 = (num / (256 * 256 * 256)) % 256
    c2 = (num / (256 * 256)) % 256
    c3 = (num / (256)) % 256
    c4 = (num / (1)) % 256
    return [c4, c3, c2, c1]

protocol_version = 0
frame_id = 0
seg_in_frame = 1
seg_id = 0
strip_id = 0
pixel_id = 0

data =  uint8_to_array(protocol_version) + \
        uint32_to_array(frame_id) + \
        uint32_to_array(seg_in_frame) + \
        uint32_to_array(seg_id) + \
        uint16_to_array(strip_id) + \
        uint16_to_array(pixel_id)

#data = data + [0, 255, 0]
data = data + [255] * 12

msg = "LedBurn" + array.array('B', data).tostring()

print ":".join("{:02x}".format(ord(c)) for c in msg)

sock.sendto(msg, (CONTROLER_IP, UDP_PORT))

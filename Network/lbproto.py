import socket
import array
import struct

class LBProtocol(object):
  
  # UDP port for communications
  UDP_PORT = 2000
  
  # protocol 8-bytes header
  HEADER = 'LedBurn\x00'

  def __init__(self, address):
    self.sock = socket.socket(socket.AF_INET, # Internet
                              socket.SOCK_DGRAM) # UDP
    self.frameid = 0
    self.address = address
  
  
  def send_simple(self, strip_id, rgb_array, pixel_id=0, **kwargs):

    # protocol header
    msg = self.HEADER 
    
    # header details
    msg += struct.pack('>I', self.frameid)
    self.frameid += 1200

    # simple send, only 1 segment
    msg += struct.pack('<I', 1)
    msg += struct.pack('<I', 0)

    # strip address and pixel offset
    msg += struct.pack('<H', strip_id)
    msg += struct.pack('<H', pixel_id)

    # data payload
    msg += array.array('B', rgb_array).tostring()

    if 'debug' in kwargs and kwargs['debug']:
      print ":".join("{:02x}".format(ord(c)) for c in msg)

    self.sock.sendto(msg, (self.address, self.UDP_PORT))
    

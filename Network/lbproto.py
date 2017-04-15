import socket
import array
import struct
import math
import ipdb

class LBProtocol(object):
  
  # UDP port for communications
  UDP_PORT = 2000
  
  # protocol 8-bytes header
  HEADER = 'LedBurn\x00'

  # packet split size by leds (note each led is 3 bytes)
  SEGMENT_SIZE = 300 * 3

  def __init__(self, address):
    self.sock = socket.socket(socket.AF_INET, # Internet
                              socket.SOCK_DGRAM) # UDP
    self.frameid = 0
    self.address = address
  
  
  def send_simple(self, strip_id, rgb_array, pixel_id=0, segments=1, segment_id=0, **kwargs):

    # protocol header
    msg = self.HEADER 
    
    if segments == 1 or segments > 1 and segment_id == 0:
      self.frameid += 1200

    # header details
    msg += struct.pack('<I', self.frameid)

    # simple send, only 1 segment
    msg += struct.pack('<I', segments)
    msg += struct.pack('<I', segment_id)

    # strip address and pixel offset
    msg += struct.pack('<H', strip_id)
    msg += struct.pack('<H', pixel_id)

    # data payload
    msg += array.array('B', rgb_array).tostring()

    if 'debug' in kwargs and kwargs['debug']:
      print "frame_id: %d, segments: %d, segment_id: %d, strip_id: %d, pixel_id: %d" % \
            (self.frameid, segments, segment_id, strip_id, pixel_id)
      print ":".join("{:02x}".format(ord(c)) for c in msg)

    self.sock.sendto(msg, (self.address, self.UDP_PORT))
    

  def send(self, strip_id, rgb_array, **kwargs):
    
    # calculate number of packets (send_simple commands)
    segments = int(math.ceil(float(len(rgb_array)) / self.SEGMENT_SIZE))

    for segment_id in xrange(segments):
      # calculate start and end of segments
      start_of_segment = segment_id * self.SEGMENT_SIZE 
      end_of_segment = min(start_of_segment + self.SEGMENT_SIZE, len(rgb_array))

      # send sub array of pixels
      seg_array = rgb_array[start_of_segment:end_of_segment]
      self.send_simple(strip_id, seg_array, segments=segments, segment_id=segment_id, **kwargs)


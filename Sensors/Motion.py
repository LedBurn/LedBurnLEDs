
import socket

import ReadRemoteUpd

class Motion:

    def __init__(self):
        # temp sensor
        self.sock = ReadRemoteUpd.create_udp_listen_sock(5006)
        self.motionAccum = 0

    def get_has_motion(self):
        motionRead = ReadRemoteUpd.read_non_blocking_udp(self.sock)
        if (motionRead != -127):
            self.motionAccum += motionRead




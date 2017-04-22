
import socket

import ReadRemoteUpd

class Temperature:

    def __init__(self):
        # temp sensor
        self.sock = ReadRemoteUpd.create_udp_listen_sock(5005)
        self.start_temp = -127
        self.temperature = -127

    def get_temperature(self):
        tempRead = ReadRemoteUpd.read_non_blocking_udp(self.sock)
        if (tempRead != -127):
            self.temperature = tempRead
        return self.temperature


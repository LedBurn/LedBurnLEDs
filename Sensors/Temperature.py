
import datetime

import ReadRemoteUpd

class Temperature:

    def __init__(self):
        # temp sensor
        self.sock = ReadRemoteUpd.create_udp_listen_sock(5005)
        self.temperature = None
        self.last_sucessful_read_time = None

    def get_temperature(self):
        tempRead = ReadRemoteUpd.read_non_blocking_udp(self.sock)
        if tempRead != -127 and tempRead is not None:
            self.temperature = tempRead
            if self.last_sucessful_read_time is None:
                print 'starting to receive temperature from sensor. curr value: ' + str(self.temperature)
            self.last_sucessful_read_time = datetime.datetime.now()
        elif self.last_sucessful_read_time and datetime.datetime.now() - self.last_sucessful_read_time > datetime.timedelta(seconds=30):
            print 'did not receive data from temperature sensor for more than 30 seconds!'
            self.last_sucessful_read_time = None
            self.temperature = None
        return self.temperature


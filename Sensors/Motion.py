
import datetime

import ReadRemoteUpd

class Motion:

    def __init__(self):
        # temp sensor
        self.sock = ReadRemoteUpd.create_udp_listen_sock(5006)
        self.motion_timestamps = []
        self.last_sucessful_read_time = None

    def get_has_motion(self):
        curr_time = datetime.datetime.now()
        motionRead = ReadRemoteUpd.read_non_blocking_udp(self.sock)
        if motionRead is not None:
            if self.last_sucessful_read_time is None:
                print 'got data from motion sensors, current read is: ' + str(motionRead)
            self.last_sucessful_read_time = curr_time
            self._remove_old_timestamps(curr_time)
            if motionRead == 1:
                self.motion_timestamps.append(curr_time)
        elif self.last_sucessful_read_time and curr_time - self.last_sucessful_read_time > datetime.timedelta(seconds=30):
            self.last_sucessful_read_time = None
        return len(self.motion_timestamps) > 3 if self.last_sucessful_read_time else None

    def _remove_old_timestamps(self, curr_time):
        while len(self.motion_timestamps) > 0 and curr_time - self.motion_timestamps[0] > datetime.timedelta(seconds=5):
            del self.motion_timestamps[0]




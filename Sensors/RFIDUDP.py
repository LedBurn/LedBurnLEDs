
import datetime

import ReadRemoteUpd

class RFIDUDP:

    def __init__(self):
        # temp sensor
        self.sock = ReadRemoteUpd.create_udp_listen_sock(5007)
        self.last_sucessful_read_time = None

        self.gymUID = 2362378675.0
        self.jointUID = 3223068223.0
        self.cardUID = 2121112269.0
        self.sachiMeter = None
        self.rfidTime = datetime.datetime.now()
       
    def process(self):

        curr_time = datetime.datetime.now()

        whichUID = self.get_uid()
        if whichUID is None:
            self.sachiMeter = None
        elif self.sachiMeter is None:
            self.sachiMeter = 0

        illusion_flag = False

        if (whichUID == self.jointUID):
            # print "ID MATCH!"
            # 3 seconds between detections avoids redundant consequtive detections
            if ((curr_time - self.rfidTime) > datetime.timedelta(seconds=3)):
                self.rfidTime = curr_time
                if (self.sachiMeter < 4):
                    self.sachiMeter += 1
                print "SachiMeter at " + str(self.sachiMeter)
        elif (whichUID == self.gymUID):
            if ((curr_time - self.rfidTime) > datetime.timedelta(seconds=3)):
                self.rfidTime = curr_time
                if (self.sachiMeter > -4):
                    self.sachiMeter += -1
                print "SachiMeter at " + str(self.sachiMeter)
        elif (whichUID == self.cardUID):
            if ((curr_time - self.rfidTime) > datetime.timedelta(seconds=3)):
                self.rfidTime = curr_time
                self.sachiMeter = 0
                illusion_flag = True
        else:
            if ((curr_time - self.rfidTime) > datetime.timedelta(seconds=30)):
                self.rfidTime = curr_time
                self.illusionFlag = False
                if (self.sachiMeter > 0):
                    self.sachiMeter -= 1
                elif (self.sachiMeter < 0):
                    self.sachiMeter += 1
                print "SachiMeter at " + str(self.sachiMeter)
                print "illusion flag reset to False"

        return (self.sachiMeter, illusion_flag)


    # if 0 is returned - there is communication but no read from sensor
    # if None is returned - there is no communication
    def get_uid(self):

        uidRead = ReadRemoteUpd.read_non_blocking_udp(self.sock)

        if uidRead is not None:
            if self.last_sucessful_read_time is None:
                print 'starting to receive RFID from sensor. curr value: ' + str(self.uidRead)
            self.last_sucessful_read_time = datetime.datetime.now()
            return uidRead

        elif self.last_sucessful_read_time and datetime.datetime.now() - self.last_sucessful_read_time > datetime.timedelta(seconds=30):
            print 'did not receive data from RFID sensor for more than 30 seconds!'
            self.last_sucessful_read_time = None

        if self.last_sucessful_read_time is None:
            return None
        else:
            return 0


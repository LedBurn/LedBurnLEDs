
import datetime

import ReadRemoteUpd

class RFIDUDP:

    def __init__(self):
        # temp sensor
        self.sock = ReadRemoteUpd.create_udp_listen_sock(5007)
        self.uid = None
        self.gymUID = 2362378675.0
        self.jointUID = 3223068223.0
        self.cardUID = 2121112269.0
        self.sachiMeter = 0
        self.prevSachiMeter = 0
        self.illusionFlag = False
        self.rfidTime = datetime.datetime.now()
       
    def process(self):

        curr_time = datetime.datetime.now()

        whichUID = self.get_uid()
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
                self.illusionFlag = True
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

        return (self.sachiMeter, self.illusionFlag)
            
    def get_uid(self):
        uidRead = ReadRemoteUpd.read_non_blocking_udp(self.sock)
        if uidRead is not None:
            self.uid = uidRead
            # print self.uid
        return self.uid


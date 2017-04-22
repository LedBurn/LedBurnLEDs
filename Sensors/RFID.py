IS_RPI = False

if IS_RPI:

    import MFRC522

    import datetime

    class RFID:

        def __init__(self):
            self.MIFAREReader = MFRC522.MFRC522()
            self.gymUID = [236, 237, 86, 75]
            self.jointUID = [32, 230, 68, 223]
            self.cardUID = [21, 211, 122, 69]
            self.sachiMeter = 0
            self.prevSachiMeter = 0
            self.illusionFlag = False
            self.rfidTime = datetime.datetime.now()

        def process(self):

            curr_time = datetime.datetime.now()

            whichUID = self.RFIDRead()
            if (set(whichUID) == set(self.jointUID)):
                # print "ID MATCH!"
                # 3 seconds between detections avoids redundant consequtive detections
                if ((curr_time - self.rfidTime) > datetime.timedelta(seconds=3)):
                    self.rfidTime = curr_time
                    if (self.sachiMeter < 4):
                        self.sachiMeter += 1
                    print "SachiMeter at " + str(self.sachiMeter)
            elif (set(whichUID) == set(self.gymUID)):
                if ((curr_time - self.rfidTime) > datetime.timedelta(seconds=3)):
                    self.rfidTime = curr_time
                    if (self.sachiMeter > -4):
                        self.sachiMeter += -1
                    print "SachiMeter at " + str(self.sachiMeter)
            elif (set(whichUID) == set(self.cardUID)):
                if ((self.MyTime - self.rfidTime) > datetime.timedelta(seconds=3)):
                    self.rfidTime = curr_time
                    self.sachiMeter = 0
                    self.illusionFlag = True
            else:
                if ((curr_time - self.rfidTime) > datetime.timedelta(seconds=30)):
                    self.rfidTime = curr_time
                    if (self.sachiMeter > 0):
                        self.sachiMeter -= 1
                    elif (self.sachiMeter < 0):
                        self.sachiMeter += 1
                    print "SachiMeter at " + str(self.sachiMeter)

            return (self.sachiMeter, self.illusionFlag)

        def RFIDRead(self):
            # Scan for cards
            (status, TagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL)

            # If a card is found
            if status == self.MIFAREReader.MI_OK:
                print "Card detected"
            else:
                return [0, 0, 0, 0]

            # Get the UID of the card
            (status, uid) = self.MIFAREReader.MFRC522_Anticoll()

            # If we have the UID, continue
            if status == self.MIFAREReader.MI_OK:
                return uid[0:4]
            else:
                return [0, 0, 0, 0]

                # Print UID
                # print "Card read UID: " + str(uid[0]) + "," + str(uid[1]) + "," + str(uid[2]) + "," + str(uid[3])
                # if ((uid[0]==Desired_UID[0]) & (uid[1]==Desired_UID[1]) & (uid[2]==Desired_UID[2]) & (uid[3]==Desired_UID[3])):
                # return 1
                # else:
                # return 0

else:

    class RFID:

        def __init__(self):
            pass

        def process(self):
            return (0,False)

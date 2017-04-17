import RPi.GPIO as GPIO
import temp_sense
import pir_sensor
import time
import datetime
import MFRC522


# temp_sense.temp_init()
# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

while True:
    time.sleep(1)

    # print(temp_sense.read_temp())
    pir_sensor.sense()
    MyTime = datetime.datetime.now()
    #print MyTime.second
    GoalTime = datetime.time(23,38,0)
    if MyTime.second > 50:
        print "ALARM, time passed!"

    # Scan for cards
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"

    # Get the UID of the card
    (status, uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        print "Card read UID: " + str(uid[0]) + "," + str(uid[1]) + "," + str(uid[2]) + "," + str(uid[3])

        # This is the default key for authentication
        key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        # Check if authenticated
        if status == MIFAREReader.MI_OK:
            MIFAREReader.MFRC522_Read(8)
            MIFAREReader.MFRC522_StopCrypto1()
        else:
            print "Authentication error"

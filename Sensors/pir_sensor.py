import RPi.GPIO as GPIO
from time import sleep

########################################################
# setup GPIO
########################################################

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.IN)


########################################################
# run def
########################################################
def sense1_is():
    return GPIO.input(11)

def sense2_is():
    return GPIO.input(12)

def run(sleep_time=0.5):

    while(1):
        if sense1_is() and sense2_is():
            print "I see you!"
        else:
            if sense1_is():
                print "sense 1"
            if sense2_is():
                print "sense 2"
        
        sleep(sleep_time)

def sense():

    if sense1_is() and sense2_is():
        print "I see you!"
        return 3
    elif sense1_is():
        print "sense 1"
        return 1
    elif sense2_is():
        print "sense 2"
        return 2
    else:
        #print "no sense"
        return 0
    
########################################################
# start the app
########################################################

# print "start GPIO sampling"
# run(0.3)


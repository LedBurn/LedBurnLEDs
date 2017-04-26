
class Decisions:

    MAX_HUG_REQUESTS = 2
    HUG_MAX_TEMP = 24.0
    ALREADY_HUGED_TEMP = 27.0
    TEMP_DIFF_FOR_DECISION = 2.0
    STONED_REQUESTS = 2

    def __init__(self):
        self.hug_request_count = 0
        self.stoned_request_count = 0

    # return None if no song
    # return yml if we want a song. example: return "Songs/Teletubbies.yml"
    def decide(self, start_temperature, curr_temperature, sachi_meter, illusions_flag, motion_detected):

        if self.use_temperature(curr_temperature):

            if start_temperature is None:
                start_temperature = curr_temperature

            diff_from_start = curr_temperature - start_temperature
            if diff_from_start > self.TEMP_DIFF_FOR_DECISION:
                print 'start temperature was ' + str(start_temperature) + " now its " + str(curr_temperature) +\
                    " thanking for the hug..."
                self.hug_request_count = 0
                return "HugThanks.yml"

            if curr_temperature < self.HUG_MAX_TEMP and self.hug_request_count < self.MAX_HUG_REQUESTS:
                self.hug_request_count += 1
                return "DesertChill.yml"
            elif curr_temperature > self.ALREADY_HUGED_TEMP:
                return "HuggingMe.yml"

        if illusions_flag:
            print "Ahh, i see you're looking for something special, how about this.. (play illusion song)"
            return "Live Fully Now - Alan Watts.yml"
        elif (sachi_meter > 0) and (sachi_meter < 3) and self.stoned_request_count < self.STONED_REQUESTS:
            self.stoned_request_count += 1
            print "Can someone pass me the sachta, i'm almost there"
            return "Sachta.yml"
        elif (sachi_meter > 2):
            print "Yooo, Ani mastul, lets get some music for the mood"
            self.stoned_request_count = 0
            return "Dreamfunk.yml"
        elif (sachi_meter < -2):
            print "man i havent been to the gym in a while, lets dance instead! (play upbeat song)"
            return "Soul Orchestra.yml"

        if motion_detected:
            print "Hey! I see I got company, let me play you a song"
            return "SeeYou.yml"

        return "Teletubbies.yml"

    def use_temperature(self, curr_temperature):
        if curr_temperature is None:
            return False
        return curr_temperature < self.HUG_MAX_TEMP or curr_temperature > self.ALREADY_HUGED_TEMP
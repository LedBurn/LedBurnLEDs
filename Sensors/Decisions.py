
class Decisions:

    MAX_HUG_REQUESTS = 2
    HUG_MAX_TEMP = 24.0
    ALREADT_HUGED_TEMP = 27.0
    TEMP_DIFF_FOR_DECISION = 2.0

    def __init__(self):
        self.start_temperature = None
        self.hug_request_count = 0

    #r eturn None if no song
    # return yml if we want a song. example: return "Songs/Teletubbies.yml"
    def decide(self, curr_temperature):

        if self.use_temperature(curr_temperature):

            if self.start_temperature is None:
                self.start_temperature = curr_temperature

            diff_from_start = curr_temperature - self.start_temperature
            if diff_from_start > self.TEMP_DIFF_FOR_DECISION:
                print 'start temperature was ' + str(self.start_temperature) + " now its " + str(curr_temperature) +\
                    " thanking for the hug..."
                return "HugThanks.yml"

            if curr_temperature < self.HUG_MAX_TEMP and self.hug_request_count < self.MAX_HUG_REQUESTS:
                self.hug_request_count += 1
                return "DesertChill.yml"




        return "Teletubbies.yml"

    def use_temperature(self, curr_temperature):
        if curr_temperature is None:
            return False
        return curr_temperature < self.HUG_MAX_TEMP or curr_temperature > self.ALREADT_HUGED_TEMP
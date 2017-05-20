import datetime
import random
import platform

class InputType:
    TEMPERATURE = 0
    SACHI = 1
    MOTION = 2

class Decisions:

    MAX_HUG_REQUESTS = 2
    HUG_MAX_TEMP = 26.0
    ALREADY_HUGED_TEMP = 27.0
    TEMP_DIFF_FOR_DECISION = 0.2
    STONED_REQUESTS = 2

    ALL_SONGS = ['bao.yml', 'Dreamfunk.yml', 'exile.yml', 'nisim.yml', 'Soul Orchestra.yml', 'space.yml',
               'strawberry.yml', 'TATRAN - Shvat.yml', 'Teletubbies.yml', 'wish.yml', 'Faceplant.yml',
               'SweetChild.yml']

    def __init__(self):
        self.hug_request_count = 0
        self.stoned_request_count = 0
        self.last_req_time = None

        self.start_temperature = None
        self.temperature_req_time = None

        # it is ok to use transitions and full songs as you like in the time_songs map
        self.time_songs  = {datetime.datetime(2017,5,28,19,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,28,19,40,0) : ["Transitions/sundown.yml", "wish.yml"], datetime.datetime(2017,5,28,20,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,28,21,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,28,22,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,28,23,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,29,0,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,29,1,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,29,2,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,29,3,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,29,4,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,29,5,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,29,5,35,0) : [random.choice(["Transitions/sunrise.yml","Transitions/sunrise_hebrew.yml"]), "wish.yml"], datetime.datetime(2017,5,29,6,0,0) : ["Transitions/hour.yml", "wish.yml"], \
                            datetime.datetime(2017,5,29,19,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,29,19,40,0) : ["Transitions/sundown.yml", "wish.yml"], datetime.datetime(2017,5,29,20,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,28,21,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,29,22,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,29,23,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,30,0,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,30,1,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,30,2,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,30,3,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,30,4,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,30,5,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,30,5,35,0) : [random.choice(["Transitions/sunrise.yml","Transitions/sunrise_hebrew.yml"]), "wish.yml"], datetime.datetime(2017,5,30,6,0,0) : ["Transitions/hour.yml", "wish.yml"], \
                            datetime.datetime(2017,5,30,19,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,30,19,40,0) : ["Transitions/sundown.yml", "wish.yml"], datetime.datetime(2017,5,30,20,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,28,21,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,30,22,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,30,23,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,31,0,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,31,1,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,31,2,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,31,3,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,31,4,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,31,5,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,31,5,35,0) : [random.choice(["Transitions/sunrise.yml","Transitions/sunrise_hebrew.yml"]), "wish.yml"], datetime.datetime(2017,5,31,6,0,0) : ["Transitions/hour.yml", "wish.yml"], \
                            datetime.datetime(2017,5,31,19,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,31,19,40,0) : ["Transitions/sundown.yml", "wish.yml"], datetime.datetime(2017,5,31,20,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,28,21,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,31,22,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,5,31,23,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,6,1,0,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,6,1,1,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,6,1,2,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,6,1,3,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,1,1,4,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,6,1,5,0,0) : ["Transitions/hour.yml", "wish.yml"], datetime.datetime(2017,6,1,5,35,0) : [random.choice(["Transitions/sunrise.yml","Transitions/sunrise_hebrew.yml"]), "wish.yml"], datetime.datetime(2017,6,1,6,0,0) : ["Transitions/hour.yml", "wish.yml"] \
                            }
        self.clear_old_time_events()

        self.songs_stats = {yml:0 for yml in self.ALL_SONGS}
        self.last_songs = []

        # curr_input is None or something from InputType
        self.curr_input = None

    # return None if no song
    # return yml if we want a song. example: return "Songs/Teletubbies.yml"
    def decide(self, curr_temperature, sachi_meter, illusions_flag, motion_detected):

        if curr_temperature is None:
            self.start_temperature = None

        # we should not work during the day when there is light, it could damage the leds.
        # we plan to disconnect electricity during the day, but if that fails, make sure the leds are not on and heating
        if not self.check_valid_hour_in_day():
            return ['silence.yml']

        next_song = self.decide_by_input(curr_temperature, sachi_meter, illusions_flag, motion_detected)
        if next_song is not None:
            self.start_temperature = curr_temperature
        return next_song


    def decide_by_input(self, curr_temperature, sachi_meter, illusions_flag, motion_detected):

        if self.curr_input is None:

            # time has a special status - it is chosen before all others
            next_songs = self.decide_by_time()
            if next_songs is not None:
                print 'next songs are chosen by time to be: ' + str(next_songs)
                # notice - we do not check here for statistics and if songs were just played
                # it is possible for songs to repeat themselves - we are OK with that :)
                for yml in next_songs:
                    self.mark_next_song(yml)
                return next_songs

            self.curr_input = self.chose_next_input(sachi_meter, curr_temperature)

        if self.curr_input == InputType.SACHI:
            next_songs = self.decide_by_RFID(illusions_flag, sachi_meter)
            return next_songs

        if self.curr_input == InputType.TEMPERATURE:
            next_song = self.decide_by_temperature(curr_temperature)
            return next_song

        if self.curr_input == InputType.MOTION:
            next_song = self.decide_by_motion(motion_detected)
            if next_song is not None:
                return next_song

        return ['sheep.yml', self.choose_and_validate_next_song()]


    def chose_next_input(self, sachi_meter, curr_temperature):
        # if not the time, we will choose an input source since we don't have one
        if sachi_meter is not None and random.random() < 0.3:
            print 'will use input selection of SACHI'
            return InputType.SACHI

        if self.use_temperature(curr_temperature) and random.random() < 0.3:
            print 'will use input selection of TEMPERATURE'
            return InputType.TEMPERATURE

        self.curr_input = None
        print 'will do sheep voice'
        return None

    def mark_next_song(self, yml):
        if yml not in self.songs_stats:
            return
        self.songs_stats[yml] = self.songs_stats[yml] + 1
        if len(self.last_songs) >= 2:
            del self.last_songs[0]
        self.last_songs.append(yml)

        # once we play a song, we forget about previous interactions with RFID.
        # so we don't get stuck with these values
        self.stoned_request_count = 0
        self.hug_request_count = 0
        self.last_req_time = None

        self.curr_input = None

    def check_song_valid(self, yml):
        if yml not in self.songs_stats:
            return True
        print 'last played songs are: ' + str(self.last_songs) + " checking if " + str(yml) + " is valid to be next"
        if yml in self.last_songs:
            return False
        else:
            self.mark_next_song(yml)
            return True

    def choose_and_validate_next_song(self):
        max_attempts = 50
        while True:
            next_song = self.choose_next_song()
            valid = self.check_song_valid(next_song)
            if valid or max_attempts == 0:
                print 'next valid song chosen! it is ' + str(next_song)
                return next_song
            max_attempts = max_attempts - 1

    def choose_next_song(self):
        min_times_played = min([c for c in self.songs_stats.itervalues()])
        relevant_songs = [yml for yml, times in self.songs_stats.iteritems() if times == min_times_played]
        print 'choosing from the following list which are played only ' + str(min_times_played) + ' times since started: ' + str(relevant_songs)
        next_song = random.choice(relevant_songs)
        return next_song

    # maybe we started after some of the times already happened? don't use them!
    def clear_old_time_events(self):
        new_times = {}
        for t,s in self.time_songs.iteritems():
            if datetime.datetime.now() < t:
                new_times[t] = s
        self.time_songs = new_times

    def decide_by_motion(self, motion_detected):
        if motion_detected:
            print "Hey! I see I got company, let me play you a song"
            return ["see_you.yml"]
        return None

    def use_temperature(self, curr_temperature):
        if curr_temperature is None:
            return False
        return curr_temperature < self.HUG_MAX_TEMP or curr_temperature > self.ALREADY_HUGED_TEMP

    def decide_by_time(self):
        for t, s in self.time_songs.iteritems():
            if datetime.datetime.now() > t:
                del self.time_songs[t]
                print "time event at " + t.ctime() + " passed, playing accordingly"
                return s
        return None

    def decide_by_RFID(self, illusions_flag, sachi_meter):

        if sachi_meter is None:
            return None

        # illusions flag will finish the RFID input selection
        if illusions_flag:
            #"Ahh, i see you're looking for something special, how about this.. (play illusion song)"
            ill_song = random.choice(["LiveFullyNow.yml", "ItStartsNow.yml", "Daya.yml"])
            print 'illusions_flag set, next illusion song is ' + str(ill_song)
            return [random.choice(["Transitions/special.yml"]), ill_song, self.choose_and_validate_next_song()]

        # finish the RFID input selection
        if sachi_meter > 2:
            #"Yooo, Ani mastul, lets play some music"
            print 'sachi meter is HIGH'
            return [random.choice(["Transitions/mastul.yml"]), self.choose_and_validate_next_song()]

        # finish the RFID input selection
        if sachi_meter < -2:
            #"man i havent been to the gym in a while, i better go soon"
            print 'sachi meter is LOW'
            return [random.choice(["Transitions/gym.yml"]), self.choose_and_validate_next_song()]

        # if we are here, we are waiting fot the user to change the sachi meter.
        # tell him how it goes...

        if self.last_req_time is None or (datetime.datetime.now() - self.last_req_time) > datetime.timedelta(seconds = 20):

            if self.stoned_request_count >= self.STONED_REQUESTS:
                print 'finished all our stoned requests. chosing next song without transition'
                return [self.choose_and_validate_next_song()]

            print 'offering user to change sachi meter'

            self.stoned_request_count += 1
            self.last_req_time = datetime.datetime.now()

            if sachi_meter >= 0:
                if self.stoned_request_count == 1:
                    #TODO: bigler change this :)
                    #you see that big ol joint, can you please pass it to kivsi?
                    return [random.choice(["Transitions/joint_ask.yml","Transitions/joint_ask_hebrew.yml"])]
                else:
                    # "Can someone pass me the sachta, i'm almost there"
                    return [random.choice(["Transitions/sachta.yml","Transitions/sachta_hebrew.yml"])]
            else:
                if self.stoned_request_count == 1:
                    #TODO: bigler change this :)
                    #has anyone seen my gym chip i swear i saw it around, can you get it to the sheep mouth?
                    return [random.choice(["Transitions/gym_ask.yml","Transitions/gym_ask_hebrew.yml"])]
                else:
                    #I can't decide if I want to get stoned or go to the gym.
                    return [random.choice(["Transitions/cant_decide.yml","Transitions/cant_decide_hebrew.yml"])]

        return None

    def decide_by_temperature(self, curr_temperature):
        if curr_temperature is None:
            return [self.choose_and_validate_next_song()]

        if self.start_temperature is None:
            self.start_temperature = curr_temperature

        diff_from_start = curr_temperature - self.start_temperature
        print diff_from_start
        if diff_from_start > self.TEMP_DIFF_FOR_DECISION:
            print 'start temperature was ' + str(self.start_temperature) + " now its " + str(curr_temperature) + \
                  " thanking for the hug..."
            self.hug_request_count = 0
            return [random.choice(["Transitions/hug_thanks.yml"]), "exile.yml"]

        enough_time_since_last = self.temperature_req_time is None or (datetime.datetime.now() - self.temperature_req_time) > datetime.timedelta(seconds=15)
        if not enough_time_since_last:
            return None

        if curr_temperature < self.HUG_MAX_TEMP and self.hug_request_count < self.MAX_HUG_REQUESTS:
            self.hug_request_count += 1
            self.temperature_req_time = datetime.datetime.now()
            if self.hug_request_count == 0:
                return [random.choice(["Transitions/desert_chill.yml", "Transitions/hold_my_stick.yml", "Transitions/cold.yml"])]
            else:
                #TODO: bigler - fix this :)
                return [random.choice(["Transitions/stick_ask.yml", "Transitions/stick_ask_hebrew.yml"])]
        elif curr_temperature > self.ALREADY_HUGED_TEMP:
            return [random.choice(["Transitions/hugging_me.yml"]), "exile.yml"]

        return [self.choose_and_validate_next_song()]


    def check_valid_hour_in_day(self):

        #do it only if we are running on the RPI
        if platform.machine() != 'armv7l':
            return True

        current_hour = datetime.datetime.now().hour
        if current_hour >= 19:
            return True
        if current_hour <= 5:
            return True
        return False





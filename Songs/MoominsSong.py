
from Effects.AlwaysOnEffect import AlwaysOnEffect
from Effects.FadeOutEffect import FadeOutEffect
from Colors import Colors

import random

class MoominsSong():

    def __init__(self, sheep):
        print "Music/The - Moomins.mp3"
        self.read_time_stamps()
        self.sheep = sheep

        self.effects = []

        self.hue = 0
        self.body_part = 0
        self.body_part_dir = 1

        self.curr_effect_start = 0
        self.curr_effect_time = 1

    def get_audio_file(self):
        return "../Music/The - Moomins.mp3"

    def read_time_stamps(self):
        fname = "../AudioAnalysis/Moomins.txt"
        with open(fname) as f:
            content = f.readlines()
        self.time_stamps = [ [float(c.split()[0]), "" if len(c.split()) < 3 else c.split()[2]] for c in content]

    def apply_animation(self, song_time):
        if self.time_stamps and song_time > self.time_stamps[0][0]:
            sheep.clear()
            label = self.time_stamps[0][1]
            if label == "H":
                self.effects = [
                    AlwaysOnEffect(sheep.get_head_indexes() + sheep.get_ears_indexes(), Colors.hls_to_rgb(self.hue, 1.0, 1.0))]
            elif label == "BP":
                self.effects = [
                    AlwaysOnEffect(sheep.get_body_part_indexes(self.body_part), Colors.hls_to_rgb(self.hue, 1.0, 1.0))]
                self.body_part = (self.body_part + self.body_part_dir)
                if self.body_part == self.sheep.get_num_of_body_parts() - 1:
                    self.body_part_dir = -1
                elif self.body_part == 0:
                    self.body_part_dir = 1
            elif label == "L1":
                self.effects = [
                    AlwaysOnEffect(sheep.get_leg12_indexes(), Colors.hls_to_rgb(self.hue, 1.0, 1.0))]
                self.hue = (self.hue + 0.3) % 1
            elif label == "L2":
                self.effects = [
                    AlwaysOnEffect(sheep.get_leg34_indexes(), Colors.hls_to_rgb(self.hue, 1.0, 1.0))]
                self.hue = (self.hue + 0.3) % 1
            elif label == "W":
                self.effects = [
                    AlwaysOnEffect(sheep.get_all_indexes(), Colors.hls_to_rgb(self.hue, 1.0, 1.0))]
            else:
                print "unknown label: " + label
                self.effects = [AlwaysOnEffect(sheep.get_body_part_indexes(self.body_part), Colors.hls_to_rgb(self.hue, 1.0, 1.0))]
                self.body_part = (self.body_part + 1) % self.sheep.get_num_of_body_parts()
            self.hue = (self.hue + 0.05) % 1
            self.curr_effect_start = self.time_stamps[0][0]
            del self.time_stamps[0]
            self.curr_effect_time = (self.time_stamps[0][0] - self.curr_effect_start) if len(self.time_stamps) > 0 else 1

        time_percent = (song_time - self.curr_effect_start)/self.curr_effect_time
        for e in self.effects:
            e.apply(time_percent, sheep.get_array())


if __name__ == "__main__":

    import pygame
    import Network.LedBurnProtocol as network
    from UIElements.SmallSheep import SmallSheep

    flower = [0, 0, 0] * 550
    grass = [0, 0, 0] * 600
    sign = [0, 0, 0] * 150
    lake = [0, 0, 0] * 1800
    sheep = SmallSheep()

    frame_id = random.randint(0, 10000000)
    song = MoominsSong(sheep)

    clock = pygame.time.Clock()
    pygame.mixer.init()
    pygame.mixer.music.load(song.get_audio_file())
    pygame.mixer.music.play(0, 0)

    while pygame.mixer.music.get_busy():
        song_time = (pygame.mixer.music.get_pos() - 170)/ 1000.0
        song.apply_animation(song_time)

        network.send(frame_id,
                     flower,
                     sheep.get_array(),
                     grass,
                     sign,
                     lake)

        frame_id += 1

        clock.tick(40)


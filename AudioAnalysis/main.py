import librosa
import pygame
import random


def onset_detect(y, sr):

    # Use a default hop size of 512 frames @ 22KHz ~= 23ms
    hop_length = 512

    # This is the window length used by default in stft
    n_fft = 2048

    # run onset detection
    print('Detecting onsets...')
    onsets = librosa.onset.onset_detect(y=y,
                                        sr=sr,
                                        hop_length=hop_length)
    print("Found {:d} onsets.".format(onsets.shape[0]))

    # 'beats' will contain the frame numbers of beat events.
    onset_times = librosa.frames_to_time(onsets,
                                         sr=sr,
                                         hop_length=hop_length,
                                         n_fft=n_fft)

    return onset_times


def beat_detect(y, sr):

    # Run the default beat tracker
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

    # Convert the frame indices of beat events into timestamps
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    return beat_times


def random_color():
    print("here")
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def analyize_file(input_file):

    print('Loading ', input_file)
    y, sr = librosa.load(input_file, sr=22050)

    onset_times = onset_detect(y, sr)
    beat_times = beat_detect(y, sr)
    
    print('done!')

    return onset_times, beat_times


file_name = "5-Sleepy_Koala_-_Froggy_Woogie"
input_file = "/Users/marie/git/sheep-stars/Music/" + file_name + ".mp3"
onset_times, beat_times = analyize_file(input_file)
current_onset = -1
current_beat = -1

pygame.mixer.init()
pygame.mixer.music.load(input_file)
pygame.mixer.music.play(0, 0)

clock = pygame.time.Clock()

screen = pygame.display.set_mode([600, 400])

while pygame.mixer.music.get_busy():
        song_time = pygame.mixer.music.get_pos()
        song_time = song_time / 1000.0

        if current_onset == -1 or (song_time > onset_times[current_onset + 1]):
            current_onset += 1
            pygame.draw.rect(screen, random_color(), [0, 0, 300, 400], 0)

        if current_beat == -1 or (song_time > beat_times[current_beat + 1]):
            current_beat += 1
            pygame.draw.rect(screen, random_color(), [300, 0, 300, 400], 0)

        pygame.display.flip()

        clock.tick(50)

        for event in pygame.event.get():  # user did something
            if event.type == pygame.QUIT:
                done = True




#!/usr/bin/env python

'''
this requires an audio processing backend.
for ubuntu:
$ sudo apt-get install libav-tools
'''

import sys
import os
import librosa
import time
import numpy as np

FILE_NAME = "ChristmasDubstep"
INPUT_FILE = "../Music_Samples/" + FILE_NAME + ".mp3"


def onset_detect(y, sr):
    """ Detect onset timestamps
    """

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

    onset_times = np.insert(onset_times, 0, 0.0)  # add time 0.0 in the beginning
    return onset_times


def beat_detect(y, sr):
    """ Detect beat timestamps
    """

    # Run the default beat tracker
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

    # Convert the frame indices of beat events into timestamps
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    beat_times = np.insert(beat_times, 0, 0.0)  # add time 0.0 in the beginning
    return beat_times


def analyize_file(input_file):
    """ Analyize the audio file into onsets and beats timestamp arrays
    """
    
    if not os.path.isfile(input_file):
      print('file not found: %s' % input_file)
      sys.exit(1)

    print('Loading ', input_file)
    y, sr = librosa.load(input_file, sr=22050)

    onset_times = onset_detect(y, sr)
    beat_times = beat_detect(y, sr)
    
    print('done!')

    return onset_times, beat_times


def save_to_file(onset_times, beat_times):
    """ Save the arrays in a txt file
    """
    file_name = "mapping_" + time.strftime("%b_%d__%H_%M_%S") + ".txt"

    text_file = open(file_name, "w")
    
    text_file.write("beat_times = [")
    text_file.write(", ".join([str(a) for a in beat_times]))
    text_file.write("]")

    text_file.write("\n")

    text_file.write("onset_times = [")
    text_file.write(", ".join([str(a) for a in onset_times]))
    text_file.write("]")

    text_file.close()

    return file_name


onset_times, beat_times = analyize_file(INPUT_FILE)
save_to_file(onset_times, beat_times)






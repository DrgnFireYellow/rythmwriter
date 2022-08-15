# SPDX-FileCopyrightText: 2022-present U.N. DrgnFireYellow <ethan@milbert.dev>
#
# SPDX-License-Identifier: Apache-2.0
import simpleaudio as _sa
from time import sleep as _sleep

def _playsound(sound):
    audio = _sa.WaveObject.from_wave_file(sound)
    audio.play()

class Rythm:
    def __init__(self, beats: list) -> None:
        self.beats = beats
    def play(self) -> None:
        for i in self.beats:
            if i == "quarter":
                _playsound("assets/drum.wav")
                _sleep(1)
            elif i == "eighth":
                _playsound("assets/drum.wav")
                _sleep(0.5)
                _playsound("assets/drum.wav")
                _sleep(0.5)
            elif i == "rest":
                _sleep(1)

if __name__ == "__main__":
    rythm = Rythm(["quarter", "eighth", "rest", "quarter", "eighth"])
    rythm.play()
from Engine.Scene import *
from Engine.Components.AudioSource import *
from Engine.Components.Stopwatch import *
from Game.Components.BeatManager import BeatManager

class playArea(Scene):
    def __init__(self, app) -> None:
        super().__init__(app, "playArea")
        self.Beat = BeatManager()

    def playLevelAudio(self):
        AudioSource.createAndPlay("Levels/Example1/Example1.mp3")

    def start(self):
        self.playLevelAudio()
        self.Beat.playBeat()

    
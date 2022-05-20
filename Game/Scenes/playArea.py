from Engine.Scene import *
from Engine.Components.AudioSource import *
from Engine.Components.Stopwatch import *
from Game.Components.BeatManager import BeatManager
import threading

class playArea(Scene):
    def __init__(self, app) -> None:
        super().__init__(app, "playArea")
        self.Beat = BeatManager()

    def playLevelAudio(self):
        PLA = threading.Thread(AudioSource.createAndPlay("Levels/Example1/Example1.ogg"))
        print("a")
        PLA.start()


    def start(self):
        self.playLevelAudio()
        BPL = threading.Thread(target=self.Beat.playBeat())
        BPL.start()

    
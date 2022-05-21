from Engine.Scene import *
from Engine.Components.AudioSource import *
from Engine.Components.Stopwatch import *
from Game.Components.BeatsoundManager import *
import threading

class playArea(Scene):
    def __init__(self, app) -> None:
        super().__init__(app, "playArea")
        self.Beatsound = BeatsoundManager()

    def playAllAudio(self):
        PLA = threading.Thread(target=AudioSource.createAndPlay("Levels/Example1/Example1.ogg"))
        BPL = threading.Thread(target=self.Beatsound.playBeat())
        PLA.start()
        BPL.start()

    def drawHexagon(self):
        Hexagon = self.entityManager.addEntity("Hexagon")

    def start(self):
        self.playAllAudio()

    
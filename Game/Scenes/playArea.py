from Engine.Scene import *
from Engine.Components.AudioSource import *
from Engine.Components.Stopwatch import *
from Engine.Components.SpriteRenderer import *
from Game.Components.BeatsoundManager import *
from Game.Components.BeatManager import *
import threading

class playArea(Scene):
    def __init__(self, app) -> None:
        super().__init__(app, "playArea")
        self.Beatsound = BeatsoundManager()
        self.BeatManager = BeatManager()
        self.app = app

    def playAllAudio(self):
        PLA = threading.Thread(target=AudioSource.createAndPlay("Levels/Example1/Example1.ogg"))
        BPL = threading.Thread(target=self.Beatsound.playBeat())
        PLA.start()
        BPL.start()

    def drawBG(self):
        Hexagon = self.entityManager.addEntity("Hexagon")
        Hexagon.addComponent(SpriteRenderer("Game/Assets/HexagonBase.png"))
        Hexagon.transform.translate(-self.app.width/2.1, 0)
        Hexagon.transform.scale(0.8)


    def start(self):
        super().start()
        self.drawBG()
        # self.playAllAudio()

    
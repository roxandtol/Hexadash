from Game.Components.BeatSpawn import *
from Game.Components.Beatsound import *
from Game.Components.BeatManager import *
from Game.Components.LevelSelector import *
from Engine.Components.SpriteRenderer import *
from Engine.Components.AudioSource import *
from Engine.Components.Stopwatch import *
from Engine.Scene import *
import threading

class playArea(Scene):
    def __init__(self, app) -> None:
        super().__init__(app, "playArea")
        self.Beatsound = Beatsound()
        self.LevelSelector = LevelSelector()
        self.app = app

    def playAllAudio(self):
        PLA = threading.Thread(target=AudioSource.createAndPlay(self.LevelSelector.readAudio()))
        PLA.start()
        # BPL = threading.Thread(target=self.Beatsound.playBeat())
        # BPL.start()

    def drawBG(self):
        Hexagon = self.entityManager.addEntity("Hexagon")
        Hexagon.addComponent(SpriteRenderer("Game/Assets/HexagonBase.png"))
        Hexagon.transform.translate(-self.app.width/2.1, 0)
        Hexagon.transform.scale(0.8)


    def start(self):
        super().start()
        self.drawBG()
        self.playAllAudio()
        beatManager = self.entityManager.addEntity("BeatManager")
        beatManager.addComponent(BeatSpawn())
        

    
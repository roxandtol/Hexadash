from Engine.Scene import *
from Engine.Components.AudioSource import *

class playArea(Scene):
    def __init__(self, app, name: str) -> None:
        super().__init__(app, "playArea")

    def readLevel(self):
        file = open("Levels/Example1/Example1.HD")

        self.level = file.readlines()

    def playLevel(self):
        AudioSource.createAndPlay("Levels/Example1/")
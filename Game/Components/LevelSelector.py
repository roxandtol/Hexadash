from Engine.Components.Component import *

class LevelSelector(Component):
    def __init__(self) -> None:
        super().__init__("LevelSelector")

    def readLevel(self):
        file = open("Levels/Example1/Example1.HD")

        return file
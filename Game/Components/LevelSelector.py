from Engine.Components.Component import *

class LevelSelector(Component):
    def __init__(self) -> None:
        super().__init__("LevelSelector")

    def readLevelMap():
        file = open("Levels/Example1/Example1.HD")

        return file

    def readAudio():
        Audio = "Levels/Example1/Example1.ogg"

        return Audio
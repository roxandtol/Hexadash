from Engine.Components.Component import *
from Engine.Components.AudioSource import *
from Engine.Components.Stopwatch import *
from Game.Components.LevelSelector import *


class BeatManager(Component):
    def __init__(self) -> None:
        super().__init__("BeatManager")
        level = LevelSelector().readLevel()
        self.level = level.readlines()
        self.crono = StopWatch()

    def playBeat(self):
        level = self.level

        for i in range(len(level)):
            currentLine = level[i].split(",")
            currentLine[2] = currentLine[2].replace("\n","")
            #0: Slot
            #1: Beat length
            #2: Delay till next beat
            delayTime = int(currentLine[2])* 0.001
            AudioSource.createAndPlay("Levels/Example1/beatsound.mp3")
            time.sleep(float(delayTime))
            print("beat!")
from Engine.Components.Component import *
from Engine.Components.AudioSource import *
from Engine.Components.Stopwatch import *
from Game.Components.LevelSelector import *


class Beatsound(Component):
    def __init__(self) -> None:
        super().__init__("BeatsoundManager")
        level = LevelSelector().readLevelMap()
        self.level = level.readlines()
        self.crono = StopWatch()

    def readBPM(self):
        self.bpm = self.level[0]
        print("BPM: " + str(self.bpm))

    def playBeat(self):
        self.readBPM()
        level = self.level

        for i in range(len(level)):
            if i == 0:
                i+=1
            else:
                currentLine = level[i].split(",")
                currentLine[2] = currentLine[2].replace("\n","")
                #0: Slot
                #1: Beat length
                #2: Delay till next beat
                delayTime = int(currentLine[2])* self.bpm
                AudioSource.createAndPlay("Levels/Example1/beatsound.mp3")
                print("beat!")
                time.sleep(float(delayTime))
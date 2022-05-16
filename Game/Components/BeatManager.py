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
            # Split the values in 3 
            currentLine = level[i].split(",")
            # Remove new line and start the crono
            currentLine[2] = currentLine[2].replace("\n","")
            self.crono.start()
            CurrentTime = self.crono.currentTime()
            delayTime = int(currentLine[2]) * 0.001
            print(currentLine)
            # # Play sounds depending of the beat
            # while float(CurrentTime) <= float(delayTime):
            #     if int(currentLine[0]) == 1:
            #         print("UNO")
            #         AudioSource.createAndPlay("Levels/Example1/beatsound1.mp3")
            #     elif int(currentLine[0]) == 2:
            #         print("DOS")
            #         AudioSource.createAndPlay("Levels/Example1/beatsound2.wav")
            #     elif int(currentLine[0]) == 3:
            #         print("TRES")
            #         AudioSource.createAndPlay("Levels/Example1/beatsound3.wav")
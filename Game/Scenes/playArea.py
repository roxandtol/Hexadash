from Engine.Scene import *
from Engine.Components.AudioSource import *
from Engine.Components.Stopwatch import *

class playArea(Scene):
    def __init__(self, app) -> None:
        super().__init__(app, "playArea")
        self.crono = StopWatch()

    def readLevel(self):
        file = open("Levels/Example1/Example1.HD")

        self.level = file.readlines()

    def playLevelAudio(self):
        AudioSource.createAndPlay("Levels/Example1/Example1.mp3")

    def playLevelBeats(self):
        level = self.level
        
        for i in range(len(level)):
            currentLine = level[i].split(",")
            currentLine[2] = currentLine[2].replace("\n","")
            self.crono.start()
            CurrentTime = self.crono.currentTime()
            delayTime = int(currentLine[2]) * 0.001
            print(currentLine)
            while float(CurrentTime) <= float(delayTime):
                if int(currentLine[0]) == 1:
                    print("UNO")
                    AudioSource.createAndPlay("Levels/Example1/beatsound1.mp3")
                elif int(currentLine[0]) == 2:
                    print("DOS")
                    AudioSource.createAndPlay("Levels/Example1/beatsound2.wav")
                elif int(currentLine[0]) == 3:
                    print("TRES")
                    AudioSource.createAndPlay("Levels/Example1/beatsound3.wav")
            


    def start(self):
        self.readLevel()
        self.playLevelAudio()
        self.playLevelBeats()

    
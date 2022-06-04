from Engine.Components.SpriteRenderer import *
from Engine.Components.AudioSource import *
from Game.Components.LevelSelector import *
from Engine.Components.Component import *

class BeatManager(Component):
    def __init__(self) -> None:
        super().__init__("BeatManager")
        level = LevelSelector().readLevelMap()
        self.level = level.readlines()
        self.levelLenght = len(self.level)
        
        self.keyPos = []

    def loadKeys(self):
        keyList = []
        level = self.level

        for i in range(self.levelLenght):
            currentLine = level[i].split(",")                   #split into an array
            currentLine[2] = currentLine[2].replace("\n","")    #remove newline
            self.keyPos.append(currentLine[0])
        print(keyList)

    def spawnBeat(self):
        self.notes = [self.getEntityManager().addEntity("Note"+ str(i)) for i in range(self.levelLenght)]
        for note in self.notes:
            note.addComponent(SpriteRenderer("Game/Assets/Single.jpg", 0.5))
            note.transform.scale(0.4)

    def start(self):
        self.bpm = self.level[0]
        self.level.pop(0)
        print(self.level)
        self.loadKeys()
    
        

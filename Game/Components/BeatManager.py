from Engine.Components.SpriteRenderer import *
from Engine.Components.AudioSource import *
from Game.Components.LevelSelector import *
from Engine.Components.Component import *

class BeatManager(Component):
    def __init__(self) -> None:
        super().__init__("BeatManager")
        level = LevelSelector.readLevelMap()
        self.level = level.readlines()
        self.levelLenght = len(self.level)-1
        
        self.keyPos = []

    def loadKeys(self):
        level = self.level

        for i in range(self.levelLenght):
            currentLine = level[i].split(",")
            currentLine[2] = currentLine[2].replace("\n","")
            self.keyPos.append(int(currentLine[0]))

    def spawnBeat(self):
        self.notes = [self.getEntityManager().addEntity("Note"+ str(i)) for i in range(self.levelLenght)]
        for note in self.notes:
            placeholder = 0
            note.addComponent(SpriteRenderer("Game/Assets/Single.jpg", 0.5))
            note.transform.scale(0.4)
            print(self.keyPos)
            # if self.keyPos[placeholder] == 1:
            #     note.transform.translate(0,100)
            #     placeholder+=1 
            # if self.keyPos[placeholder] == 2:
            #     placeholder+=1
            # else:
            #     note.transform.translate(0,-100)
            #     placeholder+=1


    def start(self):
        self.bpm = self.level[0]
        self.level.pop(0)
        self.loadKeys()
        self.spawnBeat()
    
        

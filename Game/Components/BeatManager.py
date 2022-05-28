from Engine.Components.Component import *
from Game.Components.LevelSelector import *

class BeatManager(Component):
    def __init__(self) -> None:
        super().__init__("BeatManager")
        level = LevelSelector().readLevelMap()
        self.level = level.readlines()

    def loadKeys(self):
        keyList = []
        level = self.level

        for i in range(len(level)):
            if i == 0:
                i+=1
            else:
                currentLine = level[i].split(",")                   #split into an array
                currentLine[2] = currentLine[2].replace("\n","")    #remove newline
                keyList.append(self.getEntityManager().addEntity("Key"+ str(i)))

        print(keyList)


    def start(self):
        self.loadKeys()
    
        

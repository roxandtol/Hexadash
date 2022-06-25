from Engine.Components.Component import *

class Beat(Component):
    def __init__(self, beatManager, keyPos) -> None:
        super().__init__("Beat")
        self.beatManager = beatManager
        self.keyPos = keyPos
        self.width = 800
        self.height = 600

    def keySlotSetup(self):
        self.entity.transform.setScale(0.2)
        if self.keyPos == 1:
            self.entity.transform.setPosition(self.width/2,self.height/2+self.height/4)
        elif self.keyPos == 2:
            self.entity.transform.setPosition(self.width/2,self.height/2)
        elif self.keyPos == 3: 
            self.entity.transform.setPosition(self.width/2,self.height/2-self.height/4)

    def moveKeys(self):
        pass

    def start(self):
        self.keySlotSetup()
        # print(self.keyPos)
        





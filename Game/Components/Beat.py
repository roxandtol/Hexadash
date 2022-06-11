from Engine.Components.Component import *

class Beat(Component):
    def __init__(self, beatManager, keyPos) -> None:
        super().__init__("Beat")
        self.beatManager = beatManager
        self.keyPos = keyPos
        self.width = 800
        self.height = 600

    def InitialPos(self):
        if self.keyPos == 1:
            # self.entity.transform.translate(0,100)
            self.entity.transform.setPosition(0,0)
            print("test1")
        if self.keyPos == 2:
            print("test2")
        else:
            self.entity.transform.setPosition(600,800)
            print("test3")

    def update(self):
        self.entity.transform.setScale(0.2)
        if self.keyPos == 1:
            # self.entity.transform.translate(0,100)
            self.entity.transform.setPosition(self.width/2,self.height/2+self.height/3)
            print("test1")
        if self.keyPos == 2:
            print("test2")
            self.entity.transform.setPosition(self.width/2,self.height/2)
        else:
            self.entity.transform.setPosition(self.width/2,self.height/2-self.height/4)
            print("test3")   




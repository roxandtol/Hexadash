from Engine.Components.Component import *

class Beat(Component):
    def __init__(self, beatManager, keyPos) -> None:
        super().__init__("Beat")
        self.beatManager = beatManager
        self.keyPos = keyPos
        self.width = 800
        self.height = 600

    def setup(self):
        self.entity.transform.setScale(0.2)
        if self.keyPos == 1:
            print("1")
            self.entity.transform.setPosition(self.width/2,self.height/2+self.height/4)
        elif self.keyPos == 2:
            print("2")
            self.entity.transform.setPosition(self.width/2,self.height/2)
        elif self.keyPos == 3:
            print("3")   
            self.entity.transform.setPosition(self.width/2,self.height/2-self.height/4)

    def start(self):
        self.setup()
        # print(self.keyPos)
        





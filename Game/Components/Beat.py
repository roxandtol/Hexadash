from Engine.Components.Component import *

class Beat(Component):
    def __init__(self, beatManager, keyPos) -> None:
        super().__init__("Beat")
        self.beatManager = beatManager
        self.keyPos = keyPos
        self.widthBeat = self.getApplication.width
        self.heightBeat = self.getApplication.height

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
        self.entity.transform.setScale(0.4)
        if self.keyPos == 1:
            # self.entity.transform.translate(0,100)
            self.entity.transform.setPosition(self.widthBeat/2,self.heightBeat/2-self.heightBeat/4)
            print("test1")
        if self.keyPos == 2:
            print("test2")
            self.entity.transform.setPosition(self.widthBeat/2,self.heightBeat/2)
        else:
            self.entity.transform.setPosition(self.widthBeat/2,self.heightBeat/2+self.heightBeat/4)
            print("test3")   




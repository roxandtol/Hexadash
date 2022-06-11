from Engine.Components.Component import *

class Beat(Component):
    def __init__(self, beatManager) -> None:
        super().__init__("Beat")
        self.beatManager = beatManager

    def InitialPos(self):
        self.entity.transform.setScale(0.4)
        for i in range(self.keyPos):
            if self.keyPos[i] == 1:
                self.entity.transform.translate(0,100)
                print("test1")

            if self.keyPos[i] == 2:
                print("test2")

            else:
                self.entity.transform.translate(0,-100)
                print("test3")





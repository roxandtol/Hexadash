from Engine.Scene import *

class SceneManager():
    def __init__(self) -> None:
        self.scenes = []
        self.scenesStack = []

    def addScene(self, scene : Scene):
        self.scenes.append(scene)

    def init(self):
        self.changeScene(0)

    def getCurrentScene(self) -> Scene:
        return self.scenes[len(self.scenesStack) - 1]

    def changeScene(self, index : int):
        while len(self.scenesStack) > 0:
            self.popScene()
        self.scenesStack = []
        self.pushScene(index)

    def pushScene(self, index : int):
        self.scenesStack.append(self.scenes[index])
        self.scenes[index].start()

    def popScene(self):
        scene = self.scenesStack.pop()
        scene.close()
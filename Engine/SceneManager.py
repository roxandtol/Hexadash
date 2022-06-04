from Engine.Scene import Scene


class SceneManager():
    def __init__(self) -> None:
        self.scenes = []
        self.sceneStack = []
        
    def addScene(self,scene:Scene):
        self.scenes.append(scene)

    def init(self):
        if len(self.scenes) == 0:
            return False
        self.changeScene(0)
        return True

    def currentScene(self) -> Scene:
        return self.sceneStack[len(self.sceneStack) - 1]

    def changeScene(self, index:int):
        while len(self.sceneStack) > 0:
            self.popScene()
        self.sceneStack = []
        self.pushScene(index)

    def pushScene(self,index:int):
        self.sceneStack.append(self.scenes[index])
        self.currentScene().start()

    def popScene(self):
        scene = self.sceneStack.pop()
        scene.close()
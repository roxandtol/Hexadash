from Engine.Application import *
from Game.Scenes.PauseMenu import *
from Game.Scenes.MainMenu import *
from Game.Scenes.playArea import *

class Hexadash(Application):
    def __init__(self):
        super().__init__(800,600,"Hexadash")
        self.sceneManager.addScene(playArea(self))
        self.sceneManager.addScene(MainMenu(self))
        self.sceneManager.addScene(PauseMenu(self))
        self.run()
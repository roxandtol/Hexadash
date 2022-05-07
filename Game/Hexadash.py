from Engine.Application import *
from Game.Scenes.PauseMenu import *
from Game.Scenes.MainMenu import *

class Hexadash(Application):
    def __init__(self):
        super().__init__(800,600,"Hexadash",arcade.color.BLACK)

        self.sceneManager.addScene(MainMenu(self))
        self.sceneManager.addScene(PauseMenu(self))

        self.run()
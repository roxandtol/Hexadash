#This will be the main menu for the game, it will be the first scene that the player will see when the game is launched through launcher.py. 

from Engine.Scene import *
from Game.Components.MainMenuLogic import *

class MainMenu(Scene):
    def __init__(self, app) -> None:
        super().__init__(app, "MainMenu")
        self.getApplication().setBackgroundColor(arcade.color.BLACK)

    def start(self):
        super().start()

    def draw(self):
        MainMenuManager = self.entityManager.addEntity("MainMenuManager")
        MainMenuManager.addComponent(MainMenuLogic())


from Engine.Scene import *
from Game.Components.Startlogic import *

class MainMenu(Scene):
    def __init__(self, app) -> None:
        super().__init__(app, "MainMenu")
        

    def start(self):
        super().start()
        startManager = self.entityManager.addEntity("Startlogic")
        startManager.addComponent(Startlogic())


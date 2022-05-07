from Engine.Scene import *
from Game.Components.PauseManager import PauseManager

class PauseMenu(Scene):
    def __init__(self, app) -> None:
        super().__init__(app, "PauseMenu")

    def start(self):
        super().start()
        pauseManager = self.entityManager.addEntity("PauseManager")
        pauseManager.addComponent(PauseManager())
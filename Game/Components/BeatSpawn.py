from distutils.spawn import spawn
from Engine.Components.Component import *

class BeatSpawn(Component):
    def __init__(self) -> None:
        super().__init__("BeatSpawn")

    def spawnBeat(self):
        arcade.draw_text("Beat Spawn", 100, 100, arcade.color.BLUE, 20)


    def start(self):
        self.spawnBeat()
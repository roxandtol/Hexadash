from Engine.Components.Component import *
from Game.Components.BeatManager import *

class BeatSpawn(Component):
    def __init__(self) -> None:
        super().__init__("BeatSpawn")
        Beatmngr = BeatManager()
        self.level = Beatmngr.level

    def spawnBeat(self):
        self.notes = [self.getEntityManager().addEntity("Note"+ str(i)) for i in range(self.level)]
        for note in self.coins:
            note.addComponent(SpriteRenderer("GUI/EntityComponent/Games/GameTest/Assets/gold_1.png", 0.5))
            note.addComponent(AudioSource("GUI/EntityComponent/Games/GameTest/Assets/coin_sfx.mp3", 50))


    def start(self):
        print("test")

    def update(self):
        self.spawnBeat()
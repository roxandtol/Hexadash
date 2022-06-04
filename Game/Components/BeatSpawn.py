from Engine.Components.Component import *
from Hexadash.Game.Components.BeatManager import *

class BeatSpawn(Component):
    def __init__(self) -> None:
        super().__init__("BeatSpawn")

    def spawnBeat(self):
        self.notes = [self.getEntityManager().addEntity("Note"+ str(i)) for i in range(self.numCoins)]
        for coin in self.coins:
            coin.addComponent(SpriteRenderer("GUI/EntityComponent/Games/GameTest/Assets/gold_1.png", 0.5))
            coin.addComponent(AudioSource("GUI/EntityComponent/Games/GameTest/Assets/coin_sfx.mp3", 50))


    def start(self):
        print("test")

    def update(self):
        self.spawnBeat()
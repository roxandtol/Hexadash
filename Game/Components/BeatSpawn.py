from Engine.Components.Component import *
from Engine.Components.SpriteRenderer import *
from Engine.Components.AudioSource import *
from Game.Components.BeatManager import *

class BeatSpawn(Component):
    def __init__(self) -> None:
        super().__init__("BeatSpawn")
        Beatmngr = BeatManager()
        level = Beatmngr.level
        self.levelLenght = len(level)

    def spawnBeat(self):
        self.notes = [self.getEntityManager().addEntity("Note"+ str(i)) for i in range(self.levelLenght)]
        for note in self.notes:
            note.addComponent(SpriteRenderer("Game/Assets/Single.jpg", 0.5))
            note.transform.scale(0.4)
            
            # note.addComponent(AudioSource("GUI/EntityComponent/Games/GameTest/Assets/coin_sfx.mp3", 50))

    def start(self):
        print(self.levelLenght)
        self.spawnBeat()
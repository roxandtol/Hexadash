from Engine.Components.Component import *

class AudioSource(Component):
    def __init__(self, path : str, volume = 1, loop = False) -> None:
        super().__init__("AudioSource")
        self.audio = arcade.Sound(path)
        self.volume = volume
        self.loop = loop

    def play(self):
        self.audio.play(self.volume,loop=self.loop)

    def complete(self) -> bool:
        return self.audio.is_complete()

    def playing(self) -> bool:
        return self.audio.is_playing()  

    def setLoop(self, loop:bool):
        self.loop = loop

    def setVolume(self, volume :float):
        self.volume = volume
        if self.playing():
            self.audio.set_volume(volume)
            
    def stop(self):
        if self.playing():
            self.audio.stop()

    def createAndPlay(path : str, volume = 1, loop = False):
        newSound = arcade.Sound(path)
        newSound.play(volume,0,loop )
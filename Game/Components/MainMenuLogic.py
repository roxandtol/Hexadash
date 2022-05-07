from Engine.Components.Component import *
from arcade import color

class MainMenuLogic(Component):
    def __init__(self) -> None:
        super().__init__('MainMenuLogic')

    def draw(self):
        arcade.draw_text("Hexadash", self.getApplication().width/2,self.getApplication().height/2, color.WHITE, 30,anchor_x="center")

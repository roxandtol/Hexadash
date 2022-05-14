from turtle import width
from Engine.Components.Component import *
from arcade import color
import arcade.gui

class Startlogic(Component):
    def __init__(self) -> None:
        super().__init__('MainMenuLogic')

    def draw(self):
        arcade.draw_text("Hexadash", self.getApplication().width/2,self.getApplication().height/1.3, color.WHITE, 30,anchor_x="center")

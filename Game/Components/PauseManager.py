from Engine.Components.Component import *
from arcade import color

class PauseManager(Component):
    def __init__(self) -> None:
        super().__init__('PauseManager')

    def update(self):
        if self.getInputManager().getKeyDown(KeyCode.ESCAPE):
            self.getSceneManager().popScene()

    def draw(self):
        arcade.draw_text("PULSA ESCAPE PARA SEGUIR", self.getApplication().width/2,self.getApplication().height/2, color.WHITE, 30,anchor_x="center")

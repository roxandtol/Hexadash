import arcade
from Engine.EntityManager import *
from Engine.InputManager import *
from Engine.SceneManager import *


class Application(arcade.Window):
    def __init__(self, width: int = 800, height: int = 600, title: str = 'Application'):
        super().__init__(width, height, title)
        self.inputManager = InputManager()
        self.sceneManager = SceneManager()
        self.deltaTime = 0

    def update(self, deltaTime: float):
        self.deltaTime = deltaTime
        entMngr = self.sceneManager.currentScene().entityManager
        entMngr.firstUpdate()
        entMngr.update()
        entMngr.lateUpdate()
        self.inputManager.clearKeys()

    def on_draw(self):
        # Esto siempre es lo primero
        arcade.start_render()
        # Todo lo otro después
        self.sceneManager.currentScene().entityManager.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        self.inputManager.keyPressed(symbol)

    def on_key_release(self, symbol: int, modifiers: int):
        self.inputManager.keyReleased(symbol)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.inputManager.mousePos = (x,y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == 4:
            button = 1
        elif button == 1:
            button = 0
        self.inputManager.mousePressed(button)

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        if button == 4:
            button = 1
        elif button == 1:
            button = 0
        self.inputManager.mouseReleased(button)


    def run(self):
        if self.sceneManager.init():
            arcade.run()
        else:
            print("No scenes found")
            exit()

    def exit(self):
        arcade.close_window()
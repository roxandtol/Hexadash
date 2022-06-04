from arcade import key as KeyCode


class InputManager():
    def __init__(self) -> None:
        self.keys = {}
        self.keysDown = {}
        self.keysUp = {}

    def keyPressed(self, key: KeyCode):
        self.keys[key] = True
        self.keysDown[key] = True

    def keyReleased(self, key : KeyCode):
        self.keys[key] = False
        self.keysUp[key] = True

    def getKey(self, key : KeyCode):
        if key in self.keys:
            return self.keys[key]
        return False

    def getKeyDown(self, key : KeyCode):
        if key in self.keysDown:
            return self.keysDown[key]
        return False

    def getKeyUp(self, key : KeyCode):
        if key in self.keysUp:
            return self.keysUp[key]
        return False


    def clearKeys(self):
        self.keysDown.clear()
        self.keysUp.clear()
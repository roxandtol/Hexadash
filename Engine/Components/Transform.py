
class Transform():
    def __init__(self) -> None:
        self.position = (0,0)
        self.rotation = 0
        self.localScale = 1
    
    def translate(self, x : int = 0, y : int = 0):
        X,Y = self.position
        self.position = (x + X, y + Y)

    def setPosition(self, x : int, y : int):
        self.position = (x , y )

    def rotate(self, rot:float):
        self.rotation += rot

    def setRotation(self, rot:float):
        self.rotation = rot

    def scale(self, s:float):
        self.localScale *= s

    def setScale(self, s:float):
        self.localScale = s
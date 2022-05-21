from math import sqrt
from Engine.Components.Collider import Collider
from Engine.Components.Component import *


class BoxCollider(Collider):
    def __init__(self, width: int = 50, height: int = 50, debug = False) -> None:
        super().__init__("BoxCollider", debug)
        self.width = width
        self.height = height
        self.originalWidth = width
        self.originalHeight = height
        self.debugSprite = arcade.Sprite("Engine/Assets/Collider.png")

    def update(self):
        s = self.entity.transform.localScale
        self.width = self.originalWidth * s
        self.height = self.originalHeight * s

        if self.debug:
            self.debugSprite.width = self.width
            self.debugSprite.height = self.height

    def draw(self):
        super().draw()
        if self.debug:
            x,y = self.entity.transform.position
            arcade.draw_circle_filled(x + self.width/2, y, self.width * 0.05, arcade.color.GREEN)
            arcade.draw_circle_filled(x - self.width/2, y, self.width * 0.05, arcade.color.GREEN)
            arcade.draw_circle_filled(x , y + self.height/2, self.width * 0.05, arcade.color.GREEN)
            arcade.draw_circle_filled(x , y - self.height/2, self.width * 0.05, arcade.color.GREEN)


    def checkCollision(self, other: Collider) -> bool:

        posOther = other.entity.transform.position[:]
        posThis = self.entity.transform.position[:]

        if other.name == "CircleCollider":
            x = abs(posOther[0] - posThis[0])
            y = abs(posOther[1] - posThis[1])

            if x > (self.width/2 + other.rad) or y > (self.height/2 + other.rad): 
                return False 

            if x <= (self.width/2) or y <= (self.height/2): 
                return True 

            cornerDistance_sq = (x - self.width/2)**2 + (y - self.height/2)**2

            return cornerDistance_sq <= (other.rad**2)

        elif other.name == "BoxCollider":
            # collision x-axis?
            width = self.width/2 + other.width/2
            height = self.height/2 + other.height/2

            collisionX = posThis[0] + width >= posOther[0] and posOther[0] + width >= posThis[0]
            # collision y-axis?
            collisionY = posThis[1] + height >= posOther[1] and posOther[1] + height >= posThis[1]
            # collision only if on both axes
            return collisionX and collisionY

        return False

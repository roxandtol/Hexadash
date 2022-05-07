from math import sqrt
from Engine.Components.Collider import Collider
from Engine.Components.Component import *

class CircleCollider(Collider):
    def __init__(self, rad: int = 50, debug = False) -> None:
        super().__init__("CircleCollider", debug)
        self.rad = rad
        self.originalRad = rad

    def update(self):
        self.rad = self.originalRad * self.entity.transform.localScale

    def checkCollision(self, other: Collider) -> bool:

        posOther = other.entity.transform.position[:]
        posThis = self.entity.transform.position[:]
        
        if other.name == "CircleCollider":
            x = posOther[0] - posThis[0]
            y = posOther[1] - posThis[1]
            mod = sqrt(x**2 + y**2)
            if mod < self.rad + other.rad:
                return True
        elif other.name == "BoxCollider":
            x = abs(posThis[0] - posOther[0])
            y = abs(posThis[1] - posOther[1])

            if x > (other.width/2 + self.rad) or y > (other.height/2 + self.rad): 
                return False 

            if x <= (other.width/2) or y <= (other.height/2): 
                return True 

            cornerDistance_sq = (x - other.width/2)**2 + (y - other.height/2)**2

            return cornerDistance_sq <= (self.rad**2)


        return False
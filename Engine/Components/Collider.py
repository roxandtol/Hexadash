from __future__ import annotations
from Engine.Components.Component import *

class Collider(Component):
    def __init__(self, name : str, debug = False) -> None:
        super().__init__(name)
        self.debug = debug
        self.debugSprite = None
        self.collisions = []

    def checkCollision(self, other: Collider) -> bool:
        pass

    def firstUpdate(self):
       for c in self.collisions:
            c[1] = False

    def lateUpdate(self):
        erase = []
        for c in self.collisions:
            if not c[1]:
                erase.append(c)
                self.entity.onCollisionExit(c[0])

        for e in erase:
            self.collisions.remove(e)


    def onCollision(self, other: Entity):
        for c in self.collisions:
            if c[0] == other:
                c[1] = True
                return

        self.collisions.append([other,True])
        self.entity.onCollisionEnter(other)


    def draw(self):
        if self.debug:
            self.debugSprite.position = self.entity.transform.position
            self.debugSprite.angle = self.entity.transform.rotation
            self.debugSprite.draw()
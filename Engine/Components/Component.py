from __future__ import annotations
import arcade
from Engine.Entity import *
from Engine.Application import *

class Component():
    def __init__(self, name: str = "Component") -> None:
        self.name = name
        self.entity = None
        self.enabled = True

    def start(self):
        pass

    def firstUpdate(self):
        pass

    def update(self):
        pass

    def lateUpdate(self):
        pass

    def draw(self):
        pass

    def onCollision(self, other: Entity):
        pass

    def onCollisionEnter(self, other: Entity):
        pass

    def onCollisionExit(self, other: Entity):
        pass

    def getName(self)-> str:
        return self.name

    def getEntityManager(self) -> EntityManager:
        return self.entity.entityManager

    def getApplication(self) -> Application:
        return self.getEntityManager().application

    def getInputManager(self) -> InputManager:
        return self.getApplication().inputManager

    def getSceneManager(self) -> InputManager:
        return self.getApplication().sceneManager

    def setEntity(self, entity: Entity):
        self.entity = entity

    def getComponent(self, cName: str) -> Component:
        return self.entity.getComponent(cName)
from Engine.EntityManager import *

class Scene():
    def __init__(self , app , name : str) -> None:
        self.name = name
        self.entityManager = EntityManager(app)

    def start(self):
        self.entityManager.entities = []
        self.entityManager.active = True

    def close(self):
        self.entityManager.active = False
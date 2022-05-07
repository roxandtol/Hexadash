from Engine.Components.Transform import Transform

class Entity():
    def __init__(self, entityManager, name :str = 'Entity', tag : str = 'Default') -> None:
        self.name = name
        self.tag = tag
        self.transform = Transform()
        self.components = []
        self.componentsD = {}
        self.entityManager = entityManager
        self.collider = None
        self.active = True

    def firstUpdate(self):
        for component in self.components:
            if component.enabled:
                component.firstUpdate()

    def update(self):
        for component in self.components:
            if component.enabled:
                component.update()

    def lateUpdate(self):
        for component in self.components:
            if component.enabled:
                component.lateUpdate()

    def draw(self):
        for component in self.components:
            if component.enabled:
                component.draw()

    def onCollision(self, other):
        for component in self.components:
            if component.enabled:
                component.onCollision(other)

    def onCollisionEnter(self, other):
        for component in self.components:
            if component.enabled:
                component.onCollisionEnter(other)

    def onCollisionExit(self, other):
        for component in self.components:
            if component.enabled:
                component.onCollisionExit(other)


    def addComponent(self, component):
        name = component.name
        if self.getComponent(name) != None or (self.collider != None and (name == "BoxCollider" or name == "CircleCollider")):
            print("Ya existe un componente de tipo", name, "en", self.name)
            return
        
        self.components.append(component)
        self.componentsD[component.name] = component
        component.setEntity(self)
        component.start()
        
        if name == "BoxCollider" or name == "CircleCollider":
            self.collider = component

    def removeComponent(self, cName):
        component = self.getComponent(cName)
        if component == None:
            print("La entidad",self.name, "no tiene un componente de tipo", cName)
            return
        
        self.components.remove(component)
        self.componentsD[cName] = None

        if cName == "BoxCollider" or cName == "CircleCollider":
            self.collider = None


    def getComponent(self, cName):
        if cName in self.componentsD:
            return self.componentsD[cName]
        return None

    def getCollider(self):
        return self.collider

    def destroy(self):
        self.entityManager.removeEntity(self)
    
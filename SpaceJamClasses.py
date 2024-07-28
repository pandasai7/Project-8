from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task import Task

class Planet(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath) #loads model to modelNode
        self.modelNode.reparentTo(parentNode) #reparents to parentNode, likely the camera (self.render)
        self.modelNode.setPos(posVec) #sets the position of the modelNode
        self.modelNode.setScale(scaleVec) #sets the scale of the modelNode

        self.modelNode.setName(nodeName) #sets the name of the modelNode
        tex = loader.loadTexture(texPath) #loads a texture to object tex
        self.modelNode.setTexture(tex, 1) #applies the loaded texture tex to modelNode

class Universe(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath) #loads model to modelNode
        self.modelNode.reparentTo(parentNode) #reparents to parentNode, likely the camera (self.render)
        self.modelNode.setPos(posVec) #sets the position of the modelNode
        self.modelNode.setScale(scaleVec) #sets the scale of the modelNode

        self.modelNode.setName(nodeName) #sets the name of the modelNode
        tex = loader.loadTexture(texPath) #loads a texture to object tex
        self.modelNode.setTexture(tex, 1) #applies the loaded texture tex to modelNode

class Drone(ShowBase):
    droneCount = 0
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath) #loads model to modelNode
        self.modelNode.reparentTo(parentNode) #reparents to parentNode, likely the camera (self.render)
        self.modelNode.setPos(posVec) #sets the position of the modelNode
        self.modelNode.setScale(scaleVec) #sets the scale of the modelNode

        self.modelNode.setName(nodeName) #sets the name of the modelNode
        tex = loader.loadTexture(texPath) #loads a texture to object tex
        self.modelNode.setTexture(tex, 1) #applies the loaded texture tex to modelNode

class SpaceStation(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath) #loads model to modelNode
        self.modelNode.reparentTo(parentNode) #reparents to parentNode, likely the camera (self.render)
        self.modelNode.setPos(posVec) #sets the position of the modelNode
        self.modelNode.setScale(scaleVec) #sets the scale of the modelNode

        self.modelNode.setName(nodeName) #sets the name of the modelNode
        tex = loader.loadTexture(texPath) #loads a texture to object tex
        self.modelNode.setTexture(tex, 1) #applies the loaded texture tex to modelNode

class Player(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath) #loads model to modelNode
        self.modelNode.reparentTo(parentNode) #reparents to parentNode, likely the camera (self.render)
        self.modelNode.setPos(posVec) #sets the position of the modelNode
        self.modelNode.setScale(scaleVec) #sets the scale of the modelNode

        self.modelNode.setName(nodeName) #sets the name of the modelNode
        tex = loader.loadTexture(texPath) #loads a texture to object tex
        self.modelNode.setTexture(tex, 1) #applies the loaded texture tex to modelNode
    def Thrust(self, keyDown):
        if keyDown:
            self.taskMgr.add(Player.ApplyThrust(self, 'forward-thrust'), 'forward-thrust')
        else:
            self.taskMgr.remove('forward-thrust')
    def ApplyThrust(self, task):
        rate = 5
        trajectory = self.render.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)
        return Task.cont
    def SetKeyBindings(self):
        self.accept('space', self.Thrust, [1])
        self.accept('space-up', self.Thrust, [0])
    def LeftTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLeftTurn, 'left-turn')
        else:
            self.taskManager.remove('left-turn')
    def ApplyLeftTurn(self, task):
        rate = .5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont
    def setX(self, speed):
        oldPos = self.modelNode.getPos()
        newPos = oldPos + speed
        self.modelNode.setPos(newPos)
    def setY(self, speed):
        oldPos = self.modelNode.getPos()
        newPos = oldPos + speed
        self.modelNode.setPos(newPos)
    def setZ(self, speed):
        oldPos = self.modelNode.getPos()
        newPos = oldPos + speed
        self.modelNode.setPos(newPos)
    def setX(self, speed):
        oldPos = self.modelNode.getPos()
        newPos = oldPos + speed
        self.modelNode.setPos(newPos)
    def rotateLeft(self):
        self.modelNode.setHpr(0, 0, 10)
        newPos = self.modelNode.getPos()
        return newPos
        
